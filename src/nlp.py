import spacy
import json
import re
from difflib import get_close_matches

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_candidates(text):
    """
    Extract possible skills from resume using spaCy.
    Returns: set of strings
    """
    doc = nlp(text)
    candidates = set()

    # Extract noun chunks → more accurate skill phrases
    for chunk in doc.noun_chunks:
        candidates.add(chunk.text.lower().strip())

    # Extract individual meaningful tokens
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            candidates.add(token.text.lower().strip())

    return {c for c in candidates if len(c) > 1}


def load_canonical_skills(path="skills.json"):
    with open(path, "r") as f:
        return [skill.lower() for skill in json.load(f)]


def normalize_skills(candidates, canonical_skills):
    """
    Map messy extracted words to clean standard skill names.
    """
    normalized = set()

    for cand in candidates:
        match = get_close_matches(cand, canonical_skills, n=1, cutoff=0.75)
        if match:
            normalized.add(match[0])

    return list(normalized)


def estimate_years(text):
    """
    Extract years of experience (simple heuristic).
    """
    match = re.search(r"(\d+)\s+years", text.lower())
    if match:
        return int(match.group(1))
    return 0


def extract_skills_from_text(text):
    """
    Full skill extraction pipeline.
    Returns: dict
    """
    candidates = extract_candidates(text)
    canonical = load_canonical_skills()

    normalized = normalize_skills(candidates, canonical)
    years = estimate_years(text)

    return {
        "raw_candidates": list(candidates),
        "normalized_skills": normalized,
        "years_of_experience": years
    }
