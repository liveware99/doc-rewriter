
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from app.models.prompt_templates import get_prompt_template

model = ChatOllama(model="deepseek-coder:latest")

def rewrite_placeholder(requirement, placeholder):
    system_prompt, user_prompt = get_prompt_template(requirement, placeholder)
    response = model.invoke([SystemMessage(content=system_prompt), HumanMessage(content=user_prompt)])
    return response.content.strip()
