from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love dogs.",
    "I adore puppies.",
    "I enjoy programming.",
    "The database uses an index.",
    "I made pasta for dinner."
]

embeddings = model.encode(sentences)

print("Embedding dimensions:", len(embeddings[0]))

print("\nSimilarity Matrix:\n")

similarity_matrix = cos_sim(embeddings, embeddings)

print(similarity_matrix)