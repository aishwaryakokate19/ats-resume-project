from src.parsing import extract_text_from_pdf
from src.nlp import extract_skills_from_text

text = extract_text_from_pdf("demo-resumes/sample.pdf")
output = extract_skills_from_text(text)

print("\nExtracted Normalized Skills:\n", output["normalized_skills"])
print("\nYears of Experience:\n", output["years_of_experience"])
