import streamlit as st
from src.parsing import extract_text_from_pdf
from src.scoring import compute_match_score
from src.nlp import extract_skills_from_text

st.set_page_config(
    page_title="AI ATS Resume Matcher",
    page_icon="📄",
    layout="wide",
)
# ---- CUSTOM CSS ----
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        .stApp {
            background-color: #0e1117;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: #ffffff !important;
        }
        .score-box {
            padding: 20px;
            background: #1a1d24;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #333;
            margin-top: 20px;
        }
        .skill-card {
            padding: 12px;
            background: #1f2630;
            border-radius: 8px;
            color: white;
            margin-bottom: 6px;
            border: 1px solid #3a3f47;
        }
    </style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="ATS Resume Matcher", layout="wide")

st.title("📄 AI-Powered ATS Resume Matcher")
st.write("""
This ATS Resume Matcher analyzes your resume and the job description
using NLP-based skill extraction and semantic similarity scoring.  
It outputs an ATS-style match score used by modern hiring systems.
""")

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
        
        