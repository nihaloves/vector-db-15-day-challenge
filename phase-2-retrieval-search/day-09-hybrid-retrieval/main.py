# Day 9 — Hybrid Retrieval

documents = [
    "Python is a popular programming language used for software development.",
    "Python 3.13 introduced several improvements to the Python programming language.",
    "Machine learning allows computers to learn patterns from data.",
    "Vector databases store embeddings and enable semantic search.",
    "HNSW is an algorithm used for approximate nearest neighbor search.",
    "Retrieval augmented generation combines search with language models.",
]

def keyword_search(query, documents):
    query_words = query.lower().split()

    results = []

    for document in documents:
        document_lower = document.lower()

        score = sum(
            1 for word in query_words
            if word in document_lower
        )

        if score > 0:
            results.append((document, score))

    results.sort(key=lambda x: x[1], reverse=True)

    return results

query = "Python 3.13"

results = keyword_search(query, documents)

print("\nQUERY:")
print(query)

print("\nKEYWORD SEARCH RESULTS:\n")

for i, (document, score) in enumerate(results, start=1):
    print(f"{i}. Score: {score}")
    print(f"   {document}")
    print()

from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance


model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(":memory:")

collection_name = "hybrid_retrieval"

client.create_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)    

embeddings = model.encode(documents)

points = []

for i, (document, embedding) in enumerate(zip(documents, embeddings)):
    points.append(
        PointStruct(
            id=i,
            vector=embedding.tolist(),
            payload={"text": document}
        )
    )

client.upsert(
    collection_name=collection_name,
    points=points
)

def semantic_search(query, limit=3):
    query_embedding = model.encode(query)

    results = client.query_points(
        collection_name=collection_name,
        query=query_embedding.tolist(),
        limit=limit
    ).points

    return [
        (result.payload["text"], result.score)
        for result in results
    ]

semantic_results = semantic_search(query)

print("\nSEMANTIC SEARCH RESULTS:\n")

for i, (document, score) in enumerate(semantic_results, start=1):
    print(f"{i}. Score: {score:.4f}")
    print(f"   {document}")
    print()

def normalize_keyword_results(results):
    if not results:
        return {}

    max_score = max(score for _, score in results)

    return {
        document: score / max_score
        for document, score in results
    }

keyword_results = keyword_search(query, documents)

keyword_scores = normalize_keyword_results(keyword_results)

hybrid_results = []

for document, semantic_score in semantic_results:
    keyword_score = keyword_scores.get(document, 0)

    hybrid_score = (
        0.5 * keyword_score +
        0.5 * semantic_score
    )

    hybrid_results.append(
        (document, hybrid_score, keyword_score, semantic_score)
    )

hybrid_results.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nHYBRID SEARCH RESULTS:\n")

for i, (document, hybrid_score, keyword_score, semantic_score) in enumerate(
    hybrid_results,
    start=1
):
    print(f"{i}. Hybrid Score: {hybrid_score:.4f}")
    print(f"   Keyword Score: {keyword_score:.4f}")
    print(f"   Semantic Score: {semantic_score:.4f}")
    print(f"   {document}")
    print()