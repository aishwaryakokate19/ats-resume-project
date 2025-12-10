<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-ff4b4b?logo=streamlit" />
  <img src="https://img.shields.io/badge/Model-SentenceTransformers-green" />
  <img src="https://img.shields.io/badge/Status-Deployed-success" />
  <img src="https://img.shields.io/github/stars/aishwaryakokate19/ats-resume-project?style=social" />
</p>



🌟 AI-Powered ATS Resume Matcher
A complete NLP + Machine Learning project that evaluates resume–job fit using ATS-style scoring

🔗 Live App:
👉 https://ats-resume-project-fgy89ksbfmna8frf8abnjf.streamlit.app

📌 Overview

Applicant Tracking Systems (ATS) automatically screen resumes before they reach human recruiters.
This project replicates a simplified version of ATS scoring by analyzing:

Extracted text from resume & job description

Skills matching

NLP similarity between resume content & job requirements

Missing skills that reduce match score

This tool helps job seekers optimize their resume and understand how well they match a job.

🚀 Key Features
🔍 1. PDF Parsing

Uses PyMuPDF to extract clean text

Supports multi-page PDFs

Handles structured and unstructured resumes

🧠 2. NLP-Based Skill Extraction

Powered by spaCy (en_core_web_sm)

Extracts keywords, skills, and technical terms

Compares extracted skills with job description skills

🤖 3. Semantic Similarity

Uses ML sentence embeddings to measure deeper similarity between resume & job description.

📊 4. ATS Match Score

Combines:

Skill overlap score

Semantic similarity score

Missing essential skills

To generate a final ATS percentage score.

🎨 5. Streamlit UI

Clean, modern, dark-mode interface

Upload resume PDF + JD PDF

Instant match score

Downloadable analysis report

🏗️ Tech Stack
Category	Technologies
Frontend/UI	Streamlit
Backend	Python
NLP	spaCy, embeddings
PDF Parsing	PyMuPDF
Deployment	Streamlit Cloud
Version Control	Git + GitHub
📁 Project Structure
ats-resume-project/
│
├── app.py                       # Streamlit UI logic
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── skills.json                  # List of common technical skills
│
├── src/
│   ├── parsing.py               # PDF text extraction
│   ├── nlp.py                   # Skill extraction logic
│   ├── scoring.py               # ATS score calculation
│   ├── embeddings.py            # Semantic similarity embeddings
│   └── utils.py                 # Helper functions
│
└── demo-resumes/
    ├── sample_resume.pdf        # Example resume
    └── sample_jd.pdf            # Example job description

⚙️ How It Works (Step-by-Step)
1️⃣ Upload Resume + Job Description (PDF)

User uploads two PDFs.

2️⃣ Extract Text from Both Files

Using PyMuPDF (fitz):

doc = fitz.open(pdf_path)
text = "\n".join(page.get_text() for page in doc)

3️⃣ Extract Skills Using NLP

We match extracted tokens with skills from skills.json.

4️⃣ Compute Semantic Similarity

We embed text using ML model and compute cosine similarity.

5️⃣ Generate ATS Score
Final Score = (0.5 * Skill Overlap) + (0.5 * Semantic Similarity)

6️⃣ Display Results

Match percentage

Matching skills

Missing skills

Overall similarity score

🖥️ Run the Project Locally
Clone the repository
git clone https://github.com/aishwaryakokate19/ats-resume-project.git
cd ats-resume-project

Install dependencies
pip install -r requirements.txt

Run Streamlit app
streamlit run app.py

🚀 Deployment

The project is deployed on Streamlit Cloud.

To redeploy changes:

git add .
git commit -m "update"
git push origin main


Streamlit Cloud automatically rebuilds the app.

📈 Future Enhancements

Roadmap features to make the project even stronger:

🧬 Use LLaMA 3.2 or embeddings for smarter scoring

📊 Add radar charts + skill gap visualization

📝 Resume rewriting suggestions using LLM

🔎 Highlight missing keywords directly on resume

🧑‍💼 Provide job-fit explanation summary

Want these? I can help you build them too!

👩‍💻 Author

Aishwarya Kokate
NLP | Data Science | AI Projects
🔗 LinkedIn: https://www.linkedin.com/in/aishwaryakokate19/