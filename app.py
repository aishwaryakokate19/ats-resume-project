import streamlit as st
from src.parsing import extract_text_from_pdf
from src.scoring import compute_match_score
from src.nlp import extract_skills_from_text

st.set_page_config(page_title="ATS Resume Matcher", layout="wide")

st.title("📄 AI-Powered ATS Resume Matcher")
st.write("Upload a Resume PDF and Job Description PDF to get an ATS-style match score.")

# ---- FILE UPLOAD ----
resume_pdf = st.file_uploader("Upload Resume PDF", type=["pdf"])
jd_pdf = st.file_uploader("Upload Job Description PDF", type=["pdf"])

# ---- PROCESS BUTTON ----
if st.button("🔍 Analyze Match"):
    if not resume_pdf or not jd_pdf:
        st.error("Please upload BOTH a resume PDF and a job description PDF.")
    else:
        # Save uploaded files temporarily
        with open("temp_resume.pdf", "wb") as f:
            f.write(resume_pdf.read())

        with open("temp_jd.pdf", "wb") as f:
            f.write(jd_pdf.read())

        # ---- EXTRACT TEXT ----
        resume_text = extract_text_from_pdf("temp_resume.pdf")
        jd_text = extract_text_from_pdf("temp_jd.pdf")

        # ---- COMPUTE MATCH ----
        result = compute_match_score(resume_text, jd_text)

        st.subheader("📊 Final ATS Match Score")
        st.metric("Score", f"{result['final_score']}%")

        # ---- SKILL OVERLAP ----
        st.subheader("🧩 Skill Overlap")
        st.write(result["skill_overlap"])

        # ---- RESUME SKILLS ----
        st.subheader("📘 Resume Skills Extracted")
        st.write(result["resume_skills"])

        # ---- JD SKILLS ----
        st.subheader("📙 Job Description Skills Extracted")
        st.write(result["jd_skills"])

        # ---- SEMANTIC SIM ----
        st.subheader("🧠 Semantic Similarity")
        st.write(result["semantic_similarity"])
