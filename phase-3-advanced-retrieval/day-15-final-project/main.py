from fastapi import FastAPI
from pydantic import BaseModel, Field
from sentence_transformers import SentenceTransformer, CrossEncoder
import math


app = FastAPI(
    title="Advanced Semantic Search API",
    description="A retrieval system combining metadata filtering, vector search, and reranking.",
    version="1.0.0",
)


documents = [
    {
        "text": "Python is a popular programming language used for software development.",
        "topic": "python",
        "type": "general",
    },
    {
        "text": "Python 3.13 introduced several improvements to the Python programming language.",
        "topic": "python",
        "type": "documentation",
    },
    {
        "text": "FastAPI is a Python framework for building APIs.",
        "topic": "python",
        "type": "api",
    },
    {
        "text": "Java is widely used for enterprise software and backend development.",
        "topic": "java",
        "type": "general",
    },
    {
        "text": "Vector databases store embeddings and support similarity search.",
        "topic": "vector-db",
        "type": "database",
    },
    {
        "text": "Retrieval augmented generation combines search with language models.",
        "topic": "rag",
        "type": "ai",
    },
]


embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


class SearchRequest(BaseModel):
    query: str
    top_k: int = Field(default=3, ge=1, le=6)
    topic: str | None = None

def cosine_similarity(vector_a, vector_b):
    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


document_embeddings = embedding_model.encode(
    [document["text"] for document in documents]
)


def retrieve(query, topic=None, top_k=5):

    query_embedding = embedding_model.encode(query)

    candidates = []

    for document, document_embedding in zip(
        documents,
        document_embeddings
    ):

        if topic is not None and document["topic"] != topic:
            continue

        score = cosine_similarity(
            query_embedding,
            document_embedding
        )

        candidates.append({
            "text": document["text"],
            "topic": document["topic"],
            "type": document["type"],
            "retrieval_score": float(score),
        })

    candidates.sort(
        key=lambda result: result["retrieval_score"],
        reverse=True
    )

    return candidates[:top_k]


def rerank(query, candidates):

    pairs = [
        [query, candidate["text"]]
        for candidate in candidates
    ]

    if not pairs:
        return []

    scores = reranker.predict(pairs)

    results = []

    for candidate, score in zip(candidates, scores):

        results.append({
            "text": candidate["text"],
            "topic": candidate["topic"],
            "type": candidate["type"],
            "retrieval_score": candidate["retrieval_score"],
            "rerank_score": float(score),
        })

    results.sort(
        key=lambda result: result["rerank_score"],
        reverse=True
    )

    return results

@app.get("/")
def root():
    return {
        "message": "Advanced Semantic Search API is running"
    }


@app.post("/search")
def search(request: SearchRequest):

    candidates = retrieve(
        query=request.query,
        topic=request.topic,
        top_k=request.top_k,
    )

    results = rerank(
        query=request.query,
        candidates=candidates,
    )

    return {
        "query": request.query,
        "topic_filter": request.topic,
        "results": results,
    }

@app.get("/evaluate")
def evaluate():

    evaluation_dataset = [
        {
            "query": "How can I build an API using Python?",
            "relevant_topics": {"python"},
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

    results = []

    for item in evaluation_dataset:

        candidates = retrieve(
            query=item["query"],
            top_k=5,
        )

        reranked = rerank(
            query=item["query"],
            candidates=candidates,
        )

        relevant_topics = item["relevant_topics"]

        first_relevant_rank = None

        for index, result in enumerate(reranked, start=1):
            if result["topic"] in relevant_topics:
                first_relevant_rank = index
                break

        reciprocal_rank = (
            1 / first_relevant_rank
            if first_relevant_rank is not None
            else 0.0
        )

        results.append({
            "query": item["query"],
            "first_relevant_rank": first_relevant_rank,
            "reciprocal_rank": reciprocal_rank,
        })

    mrr = sum(
        result["reciprocal_rank"]
        for result in results
    ) / len(results)

    return {
        "evaluation": results,
        "mrr": mrr,
    }