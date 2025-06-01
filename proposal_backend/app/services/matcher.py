
import json
from sentence_transformers import SentenceTransformer, util

with open("app/services/placeholder_keyword_map.json", "r", encoding="utf-8") as f:
    placeholder_keyword_map = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

def match_requirement_to_placeholder(requirements, placeholder):
    keywords = placeholder_keyword_map.get(placeholder, [])
    for req in requirements:
        if any(kw.lower() in req.lower() for kw in keywords):
            return req
    req_embeddings = model.encode(requirements, convert_to_tensor=True)
    placeholder_embedding = model.encode(placeholder.replace("<", "").replace(">", "").replace("_", " "), convert_to_tensor=True)
    similarities = util.cos_sim(placeholder_embedding, req_embeddings)[0]
    best_idx = int(similarities.argmax())
    return requirements[best_idx]
