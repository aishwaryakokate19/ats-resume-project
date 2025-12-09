import spacy
import numpy as np

# Load medium-sized English model (includes embeddings)
try:
    nlp = spacy.load("en_core_web_md")
except:
    import spacy.cli
    spacy.cli.download("en_core_web_md")
    nlp = spacy.load("en_core_web_md")

def embed_text(text):
    doc = nlp(text)
    return doc.vector

def cosine_similarity(a, b):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
