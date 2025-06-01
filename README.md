# Tech Proposal Rewriter

This project automates the generation of customized technical proposals based on customer-specific compliance sheets.

## 🧠 Powered by
- Locally hosted LLM via **Ollama** (e.g., DeepSeek, LLaMA 3)
- **LangChain** for prompt management
- **FastAPI** backend
- **Streamlit** frontend for live preview and editing

---

## 💼 Features
- Upload Excel compliance sheet
- Filters only `Comply` (FC) records
- Loads original template with placeholders
- Rewrites only the placeholders using matched requirements
- Provides fallback to original content if needed
- Cleans and refines generated text
- Displays side-by-side editable preview
- Supports download of final `.docx` file

---

## 🗂 Folder Structure

```
proposal_backend/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── utils/
│   ├── templates/
│   └── main.py
│
├── original_texts.json
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

1. Install Ollama and pull the model:

```bash
ollama pull deepseek-coder:latest
```

2. Start the backend:

```bash
uvicorn app.main:app --reload
```

3. Start the frontend (Streamlit):

```bash
streamlit run ui/main.py
```

---

## 📂 Sample Files

- `tech_proposal_rewriter_template.docx`: Word template with placeholders
- `original_texts.json`: Static fallback content
- `tech_proposal_compliance_sheet.xlsx`: Example compliance input

