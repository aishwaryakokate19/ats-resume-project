from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str):
    """Return embedding vector for input text."""
    return model.encode([text], convert_to_numpy=True)[0]

def cosine_similarity(vec1, vec2):
    """Compute cosine similarity between two vectors."""
    if vec1 is None or vec2 is None:
        return 0.0

    v1 = vec1 / np.linalg.norm(vec1)
    v2 = vec2 / np.linalg.norm(vec2)

    return float(np.dot(v1, v2))
