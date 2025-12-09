from src.parsing import extract_text_from_pdf, split_sections

path = "demo-resumes/sample.pdf"

text = extract_text_from_pdf(path)
print("EXTRACTED TEXT:\n", text[:500])  # show first 500 characters

sections = split_sections(text)
print("\nSECTIONS FOUND:\n", sections.keys())
