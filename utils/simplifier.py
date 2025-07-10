import json
import re

def load_glossary(filepath):
    with open(filepath, "r") as f:
        glossary = json.load(f)
    return glossary

def simplify_text(text, glossary):
    simplified = text
    for term, meaning in glossary.items():
        pattern = r'\b' + re.escape(term) + r'\b'
        simplified = re.sub(pattern, meaning, simplified, flags=re.IGNORECASE)
    return simplified
