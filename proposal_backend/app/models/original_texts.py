
import json
import os

file_path = os.path.join(os.path.dirname(__file__), "original_texts.json")

with open(file_path, "r", encoding="utf-8") as f:
    original_texts = json.load(f)
