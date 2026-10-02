from sentence_transformers import SentenceTransformer, CrossEncoder
import math


documents = [
    "Python 3.13 introduced several improvements to the Python programming language.",
    "Python is a popular programming language used for software development.",
    "Java is widely used for enterprise software and backend development.",
    "Retrieval augmented generation combines search with language models.",
    "Vector databases store embeddings and support similarity search.",
    "FastAPI is a Python framework for building APIs.",
]


embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def cosine_similarity(vector_a, vector_b):
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def retrieve(query, top_k=5):
    query_embedding = embedding_model.encode(query)

    results = []

    for document in documents:
        document_embedding = embedding_model.encode(document)

        score = cosine_similarity(
            query_embedding,
            document_embedding
        )

        results.append({
            "text": document,
            "retrieval_score": score,
        })

    results.sort(
        key=lambda result: result["retrieval_score"],
        reverse=True
    )

    return results[:top_k]


def rerank(query, candidates):
    pairs = [
        [query, candidate["text"]]
        for candidate in candidates
    ]

    scores = reranker.predict(pairs)

    reranked_results = []

    for candidate, score in zip(candidates, scores):
        reranked_results.append({
            "text": candidate["text"],
            "retrieval_score": candidate["retrieval_score"],
            "rerank_score": float(score),
        })

    reranked_results.sort(
        key=lambda result: result["rerank_score"],
        reverse=True
    )

    return reranked_results


query = "How can I build an API using Python?"

print("=" * 70)
print("QUERY")
print("=" * 70)
print(query)

candidates = retrieve(query, top_k=5)

print("\n" + "=" * 70)
print("INITIAL RETRIEVAL")
print("=" * 70)

for index, result in enumerate(candidates, start=1):
    print(f"\n{index}. Retrieval Score: {result['retrieval_score']:.4f}")
    print(f"   {result['text']}")


reranked_results = rerank(query, candidates)

print("\n" + "=" * 70)
print("AFTER RERANKING")
print("=" * 70)

for index, result in enumerate(reranked_results, start=1):
    print(f"\n{index}. Rerank Score: {result['rerank_score']:.4f}")
    print(f"   Retrieval Score: {result['retrieval_score']:.4f}")
    print(f"   {result['text']}")