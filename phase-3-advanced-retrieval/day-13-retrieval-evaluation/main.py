from sentence_transformers import SentenceTransformer
import math


documents = [
    {
        "text": "Python is a popular programming language used for software development.",
        "topic": "python",
    },
    {
        "text": "Python 3.13 introduced several improvements to the Python programming language.",
        "topic": "python",
    },
    {
        "text": "FastAPI is a Python framework for building APIs.",
        "topic": "api",
    },
    {
        "text": "Java is widely used for enterprise software and backend development.",
        "topic": "java",
    },
    {
        "text": "Vector databases store embeddings and support similarity search.",
        "topic": "vector-db",
    },
    {
        "text": "Retrieval augmented generation combines search with language models.",
        "topic": "rag",
    },
]


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def cosine_similarity(vector_a, vector_b):
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def retrieve(query, top_k=3):
    query_embedding = model.encode(query)

    results = []

    for document in documents:
        document_embedding = model.encode(document["text"])

        score = cosine_similarity(
            query_embedding,
            document_embedding
        )

        results.append({
            "text": document["text"],
            "topic": document["topic"],
            "score": score,
        })

    results.sort(
        key=lambda result: result["score"],
        reverse=True
    )

    return results[:top_k]


evaluation_dataset = [
    {
        "query": "How can I build an API using Python?",
        "relevant_topics": {"python", "api"},
    },
    {
        "query": "What is a vector database?",
        "relevant_topics": {"vector-db"},
    },
    {
        "query": "What is retrieval augmented generation?",
        "relevant_topics": {"rag"},
    },
]


def precision_at_k(results, relevant_topics, k):
    top_results = results[:k]

    relevant_count = sum(
        1 for result in top_results
        if result["topic"] in relevant_topics
    )

    return relevant_count / k


def recall_at_k(results, relevant_topics, k):
    top_results = results[:k]

    relevant_count = sum(
        1 for result in top_results
        if result["topic"] in relevant_topics
    )

    total_relevant = sum(
        1 for document in documents
        if document["topic"] in relevant_topics
    )

    if total_relevant == 0:
        return 0.0

    return relevant_count / total_relevant


def reciprocal_rank(results, relevant_topics):
    for index, result in enumerate(results, start=1):
        if result["topic"] in relevant_topics:
            return 1 / index

    return 0.0


print("=" * 70)
print("RETRIEVAL EVALUATION")
print("=" * 70)


precision_scores = []
recall_scores = []
mrr_scores = []


for item in evaluation_dataset:

    query = item["query"]
    relevant_topics = item["relevant_topics"]

    results = retrieve(query, top_k=3)

    precision = precision_at_k(
        results,
        relevant_topics,
        k=3
    )

    recall = recall_at_k(
        results,
        relevant_topics,
        k=3
    )

    rr = reciprocal_rank(
        results,
        relevant_topics
    )

    precision_scores.append(precision)
    recall_scores.append(recall)
    mrr_scores.append(rr)

    print(f"\nQuery: {query}")

    print("\nTop Results:")

    for index, result in enumerate(results, start=1):
        print(
            f"{index}. {result['text']}"
            f" | Score: {result['score']:.4f}"
        )

    print(f"\nPrecision@3: {precision:.4f}")
    print(f"Recall@3:    {recall:.4f}")
    print(f"Reciprocal Rank: {rr:.4f}")


mean_precision = sum(precision_scores) / len(precision_scores)
mean_recall = sum(recall_scores) / len(recall_scores)
mrr = sum(mrr_scores) / len(mrr_scores)


print("\n" + "=" * 70)
print("OVERALL EVALUATION")
print("=" * 70)

print(f"\nMean Precision@3: {mean_precision:.4f}")
print(f"Mean Recall@3:    {mean_recall:.4f}")
print(f"MRR:              {mrr:.4f}")