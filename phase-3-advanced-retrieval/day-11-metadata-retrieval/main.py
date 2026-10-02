from sentence_transformers import SentenceTransformer
import math


documents = [
    {
        "text": "Python 3.13 introduced several improvements to the Python programming language.",
        "topic": "python",
        "version": "3.13",
        "type": "documentation",
    },
    {
        "text": "Python is a popular programming language used for software development.",
        "topic": "python",
        "version": "general",
        "type": "documentation",
    },
    {
        "text": "Java is widely used for enterprise software and backend development.",
        "topic": "java",
        "version": "21",
        "type": "documentation",
    },
    {
        "text": "Retrieval augmented generation combines search with language models.",
        "topic": "ai",
        "version": "general",
        "type": "research",
    },
    {
        "text": "Vector databases store embeddings and support similarity search.",
        "topic": "vector-database",
        "version": "general",
        "type": "documentation",
    },
    {
        "text": "FastAPI is a Python framework for building APIs.",
        "topic": "python",
        "version": "general",
        "type": "documentation",
    },
]


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def cosine_similarity(vector_a, vector_b):
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def metadata_matches(document, filters):
    for key, value in filters.items():
        if document.get(key) != value:
            return False

    return True


def metadata_search(query, filters=None, top_k=3):
    query_embedding = model.encode(query)

    results = []

    for document in documents:
        if filters and not metadata_matches(document, filters):
            continue

        document_embedding = model.encode(document["text"])

        score = cosine_similarity(
            query_embedding,
            document_embedding
        )

        results.append({
            "text": document["text"],
            "score": score,
            "metadata": {
                "topic": document["topic"],
                "version": document["version"],
                "type": document["type"],
            },
        })

    results.sort(key=lambda result: result["score"], reverse=True)

    return results[:top_k]


queries = [
    {
        "query": "Python programming",
        "filters": {"topic": "python"},
    },
    {
        "query": "Python API development",
        "filters": {
            "topic": "python",
            "type": "documentation",
        },
    },
    {
        "query": "Python 3.13",
        "filters": {
            "topic": "python",
            "version": "3.13",
        },
    },
]


for search in queries:
    print("=" * 60)
    print(f"QUERY: {search['query']}")
    print(f"FILTERS: {search['filters']}")
    print("=" * 60)

    results = metadata_search(
        search["query"],
        filters=search["filters"],
        top_k=3,
    )

    for index, result in enumerate(results, start=1):
        print(f"\n{index}. Similarity Score: {result['score']:.4f}")
        print(f"   Metadata: {result['metadata']}")
        print(f"   {result['text']}")

    print()



