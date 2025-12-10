# 🚀 AI-Powered ATS Resume Matcher

A Streamlit-based web application that analyzes **Resume PDFs** and **Job Description PDFs** to compute an **ATS-style match score** using NLP techniques, skill extraction, and sentence embeddings.

🔗 **Live App:** https://ats-resume-project-fgy89ksbfmna8frf8abnjf.streamlit.app/  
📁 **GitHub Repo:** https://github.com/aishwaryakokate19/ats-resume-project

---

## ⭐ Features

- 📄 Upload Resume PDF & Job Description PDF  
- 🤖 Extract text using PyMuPDF  
- 🧠 NLP-based skill extraction  
- 🔍 Sentence Transformer Embeddings  
- 🎯 Semantic similarity scoring  
- 📊 Final ATS-style match score  
- 📉 Skill gap analysis  
- ☁️ Fully deployed on Streamlit Cloud  

---

## 🏗️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | Python |
| NLP | spaCy, Sentence-Transformers |
| Embeddings | all-MiniLM-L6-v2 |
| Parsing PDFs | PyMuPDF, pdf2image |
| Deployment | Streamlit Cloud |

---

## 📂 Project Structure

```
ats-resume-project/
│
├── app.py
├── README.md
├── requirements.txt
├── pyproject.toml
├── .streamlit/
│   └── runtime.txt
│   └── config.toml
│
├── src/
│   ├── parsing.py
│   ├── nlp.py
│   ├── scoring.py
│   ├── embeddings.py
│   ├── utils.py
│
└── demo-resumes/
```

---

## ⚙️ Installation (Run Locally)

Clone the repo:

```bash
git clone https://github.com/aishwaryakokate19/ats-resume-project.git
cd ats-resume-project
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## 🧪 How It Works

1. **PDF Parsing**  
   Extract text from PDFs using PyMuPDF.

2. **Skill Extraction**  
   Extract common professional skills using spaCy patterns + a skills JSON list.

3. **Embedding Generation**  
   Convert text into numerical vectors using Sentence-Transformers.

4. **Similarity Matching**  
   Cosine similarity determines semantic relatedness.

5. **Final ATS Score**  
   Combination of:
   - Skill overlap
   - JD missing skills
   - Semantic similarity

---

## 📉 Skill Gap Report

The app highlights:

- Skills in your resume ✔️  
- Skills missing that the JD requires ❌  
- Suggestions to improve your match score 📈  

---

## 📸 Screenshots

(Add your screenshot here later)

---

## 🛠️ To-Do (Future Enhancements)

- Add LLaMA/OpenAI model for smart recommendations  
- Resume improvement suggestions  
- Automatic resume rewriting  
- Multi-page report download as PDF  

---

## 👩‍💻 Author

**Aishwarya Kokate**

- 🔗 GitHub: https://github.com/aishwaryakokate19  
- 💼 Project: ATS Resume Matcher  

---

## ⭐ Support

If you like this project, consider giving the repo a **star ⭐ on GitHub**!
