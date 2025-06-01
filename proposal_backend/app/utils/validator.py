
def is_valid_response(text: str, required_keywords: list[str]) -> bool:
    text = text.lower()
    if len(text.split()) < 40 or "sorry" in text or "unclear" in text:
        return False
    return all(keyword in text for keyword in required_keywords)
