from src.parsing import extract_text_from_pdf
from src.scoring import compute_match_score

# Load resume PDF
resume_text = extract_text_from_pdf("demo-resumes/sample.pdf")

# Load job description PDF
job_desc_text = extract_text_from_pdf("demo-resumes/jd.pdf")

# Compute match score
score = compute_match_score(resume_text, job_desc_text)
print(score)
