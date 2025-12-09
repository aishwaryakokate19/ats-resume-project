import fitz  # PyMuPDF

def extract_text_from_pdf(path: str) -> str:
    """
    Extracts text from a PDF file using PyMuPDF.
    Works for most digital (non-scanned) resume PDFs.
    Returns raw text as a single string.
    """
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text


def split_sections(text: str) -> dict:
    """
    Splits resume text into logical sections by detecting common headers.
    Example output:
    {
        "SKILLS": "...",
        "EXPERIENCE": "...",
        "EDUCATION": "...",
        ...
    }
    """
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    sections = {}
    current = "GENERAL"

    sections[current] = []

    for line in lines:
        upper = line.upper()

        # If line looks like a section header
        if any(h in upper for h in [
            "EDUCATION",
            "EXPERIENCE",
            "WORK EXPERIENCE",
            "PROJECTS",
            "SKILLS",
            "CERTIFICATIONS"
        ]):
            current = upper  # new section
            sections[current] = []
        else:
            sections[current].append(line)

    return {k: "\n".join(v) for k, v in sections.items()}
