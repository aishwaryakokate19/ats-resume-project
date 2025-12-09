from src.embeddings import embed_text, cosine_similarity
from src.nlp import extract_skills_from_text

def compute_match_score(resume_text, job_desc_text):
    """
    Combines embedding similarity + skill overlap + experience estimate.
    Returns a final score between 0–100.
    """

    # 1) Embedding similarity
    resume_vec = embed_text(resume_text)
    jd_vec = embed_text(job_desc_text)
    semantic_sim = cosine_similarity(resume_vec, jd_vec)

    # 2) Skill extraction
    resume_skills = extract_skills_from_text(resume_text)
    jd_skills = extract_skills_from_text(job_desc_text)

    resume_skill_set = set(resume_skills["normalized_skills"])
    jd_skill_set = set(jd_skills["normalized_skills"])

    # 3) Skill overlap
    overlap = resume_skill_set & jd_skill_set
    if len(jd_skill_set) > 0:
        skill_score = len(overlap) / len(jd_skill_set)
    else:
        skill_score = 0

    # 4) Experience handling
    years = resume_skills["years_of_experience"]
    exp_score = min(years / 5, 1.0)  # caps at 1.0

    # 5) Weighted final score
    final_score = (
        0.60 * semantic_sim +
        0.30 * skill_score +
        0.10 * exp_score
    )

    return {
        "final_score": round(final_score * 100, 2),
        "semantic_similarity": semantic_sim,
        "skill_overlap": list(overlap),
        "resume_skills": list(resume_skill_set),
        "jd_skills": list(jd_skill_set)
    }
