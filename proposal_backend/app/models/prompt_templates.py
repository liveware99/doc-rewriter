
import json
import os

def get_prompt_template(requirement, placeholder):
    system_prompt = (
        "You are an expert documentation writer. "
        "Write a formal, concise, and confident paragraph to rewrite the given original text "
        "based on the customer's requirement. Avoid using headings, apologies, or unclear phrases. "
        "Assume the content will be inserted directly into a customer-facing technical proposal."
    )

    # Load original texts from JSON
    config_path = os.path.join(os.path.dirname(__file__), "../../config/original_texts.json")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            original_texts = json.load(f)
        placeholder_context = original_texts.get(placeholder, "").strip()
    except Exception:
        placeholder_context = ""

    # Add original text as inspiration if available
    if placeholder_context:
        system_prompt += f" Here is the current original text to inspire you:\n{placeholder_context}"

    user_prompt = (
        f'The customer requirement is:\n"{requirement}"\n\n'
        f"Rewrite a content to replace the current original text."
    )

    return system_prompt, user_prompt
