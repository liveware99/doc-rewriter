
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from app.services.excel_parser import extract_comply_records
from app.services.template_handler import load_template, extract_placeholders, replace_placeholder
from app.services.deepseek_writer import rewrite_placeholder
from app.services.matcher import match_requirement_to_placeholder
from app.utils.cleaner import clean_text
from app.utils.validator import is_valid_response
from app.models.original_texts import original_texts
import os

router = APIRouter()

@router.post("/rewrite-proposal")
async def rewrite_proposal(file: UploadFile = File(...)):
    path = f"uploads/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())

    comply_df = extract_comply_records(path)
    requirements = comply_df["Requirement"].tolist()
    doc = load_template("templates/technical_proposal_template.docx")
    placeholders = extract_placeholders(doc)

    for placeholder in placeholders:
        original = original_texts.get(placeholder, "")
        requirement = match_requirement_to_placeholder(requirements, placeholder)
        generated = rewrite_placeholder(requirement, placeholder)
        cleaned = clean_text(generated)
        final_text = cleaned if is_valid_response(cleaned, requirement.lower().split()) else original
        replace_placeholder(doc, placeholder, final_text)

    output_name = f"customized_{file.filename.replace('.xlsx', '.docx')}"
    output_path = f"output/{output_name}"
    doc.save(output_path)
    return FileResponse(output_path, media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document', filename=output_name)
