
import re

def clean_text(input_text):
    input_text = re.sub(r'<think>.*?</think>', '', input_text, flags=re.DOTALL)
    input_text = re.sub(r'\s+', ' ', input_text).strip()
    input_text = re.sub(r"(?i)(I'm sorry|your request is unclear|please provide).*", "", input_text)
    return input_text.strip()
