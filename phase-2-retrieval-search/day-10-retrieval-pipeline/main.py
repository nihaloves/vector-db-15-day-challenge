# Day 10 — Retrieval Pipeline

documents = [
    "Python is a popular programming language used for software development.",
    "Python 3.13 introduced several improvements to the Python programming language.",
    "Machine learning allows computers to learn patterns from data.",
    "Vector databases store embeddings and enable semantic search.",
    "HNSW is an algorithm used for approximate nearest neighbor search.",
    "Retrieval augmented generation combines search with language models.",
]

print("Documents loaded:", len(documents))

from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(":memory:")

collection_name = "retrieval_pipeline"

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

print("Documents indexed:", len(points))

def semantic_retrieve(query, limit=3):
    query_embedding = model.encode(query)

    results = client.query_points(
        collection_name=collection_name,
        query=query_embedding.tolist(),
        limit=limit
    ).points

    return [
        {
            "text": result.payload["text"],
            "score": result.score
        }
        for result in results
    ]
import re


def keyword_retrieve(query):
    query_words = re.findall(r"\b\w+\b", query.lower())

    results = []

    for document in documents:
        document_words = set(
            re.findall(r"\b\w+\b", document.lower())
        )

        score = sum(
            1 for word in query_words
            if word in document_words
        )

        if score > 0:
            results.append(
                {
                    "text": document,
                    "score": score
                }
            )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results

def normalize_keyword_results(results):
    if not results:
        return {}

    max_score = max(
        result["score"]
        for result in results
    )

    return {
        result["text"]: result["score"] / max_score
        for result in results
    }

def retrieval_pipeline(query):
    semantic_results = semantic_retrieve(query, limit=3)
    keyword_results = keyword_retrieve(query)

    keyword_scores = normalize_keyword_results(keyword_results)

    hybrid_results = []

    for result in semantic_results:
        document = result["text"]
        semantic_score = result["score"]
        keyword_score = keyword_scores.get(document, 0)

        hybrid_score = (
            0.5 * keyword_score +
            0.5 * semantic_score
        )

        hybrid_results.append(
    {
        "text": document,
        "score": hybrid_score,
        "keyword_score": keyword_score,
        "semantic_score": semantic_score
    }
)

    hybrid_results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return hybrid_results


query = "Python 3.13"

results = retrieval_pipeline(query)

print("\nQUERY:")
print(query)

print("\nRETRIEVED DOCUMENTS:\n")

for i, result in enumerate(results, start=1):
    print(f"{i}. Hybrid Score: {result['score']:.4f}")
    print(f"   Keyword Score: {result['keyword_score']:.4f}")
    print(f"   Semantic Score: {result['semantic_score']:.4f}")
    print(f"   {result['text']}")
    print()