import numpy as np
from sentence_transformers import SentenceTransformer


# -----------------------------------
# 1. Similarity / Distance Functions
# -----------------------------------

def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


def euclidean_distance(a, b):
    return np.linalg.norm(a - b)


def dot_product(a, b):
    return np.dot(a, b)


# -----------------------------------
# 2. Basic Vector Experiment
# -----------------------------------

def vector_experiment():
    vector_a = np.array([1, 2, 3])
    vector_b = np.array([1, 2, 3])
    vector_c = np.array([3, 2, 1])

    print("=== Basic Vector Comparison ===")

    print("\nCosine Similarity:")
    print("A vs B:", cosine_similarity(vector_a, vector_b))
    print("A vs C:", cosine_similarity(vector_a, vector_c))

    print("\nEuclidean Distance:")
    print("A vs B:", euclidean_distance(vector_a, vector_b))
    print("A vs C:", euclidean_distance(vector_a, vector_c))

    print("\nDot Product:")
    print("A vs B:", dot_product(vector_a, vector_b))
    print("A vs C:", dot_product(vector_a, vector_c))


# -----------------------------------
# 3. Semantic Search
# -----------------------------------

def semantic_search():
    sentences = [
        "Python is a popular programming language.",
        "I love learning how to code.",
        "The beach was beautiful today.",
        "Machine learning uses data to make predictions.",
        "I enjoy playing football with my friends."
    ]

    query = "I want to learn programming."

    print("\n=== Semantic Search ===")
    print("Query:", query)

    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Generate embeddings
    embeddings = model.encode(sentences)
    query_embedding = model.encode(query)

    print("Number of sentences:", len(sentences))
    print("Embedding dimensions:", len(embeddings[0]))

    # Calculate similarity
    results = []

    for sentence, embedding in zip(sentences, embeddings):
        score = cosine_similarity(query_embedding, embedding)
        results.append((score, sentence))

    # Sort by highest similarity
    results.sort(reverse=True)

    print("\nSemantic Search Results:")
    print("-----------------------")

    for score, sentence in results:
        print(f"{score:.4f} → {sentence}")

    # Top-K
    k = 3

    print(f"\nTop {k} Results:")
    print("--------------")

    for score, sentence in results[:k]:
        print(f"{score:.4f} → {sentence}")


# -----------------------------------
# 4. Main
# -----------------------------------

if __name__ == "__main__":
    vector_experiment()
    semantic_search()