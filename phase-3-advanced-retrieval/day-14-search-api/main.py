from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import math


app = FastAPI(
    title="Vector Search API",
    description="A simple semantic search API using sentence embeddings.",
    version="1.0.0",
)


documents = [
    "Python is a popular programming language used for software development.",
    "Python 3.13 introduced several improvements to the Python programming language.",
    "FastAPI is a Python framework for building APIs.",
    "Java is widely used for enterprise software and backend development.",
    "Vector databases store embeddings and support similarity search.",
    "Retrieval augmented generation combines search with language models.",
]


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    query: str
    top_k: int = Field(default=3, ge=1, le=6)


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


document_embeddings = model.encode(documents)


def search_documents(query, top_k):
    query_embedding = model.encode(query)

    results = []

    for document, document_embedding in zip(
        documents,
        document_embeddings
    ):
        score = cosine_similarity(
            query_embedding,
            document_embedding
        )

        results.append({
            "text": document,
            "score": float(score),
        })

    results.sort(
        key=lambda result: result["score"],
        reverse=True
    )

    return results[:top_k]


@app.get("/")
def root():
    return {
        "message": "Vector Search API is running"
    }


@app.post("/search")
def search(request: SearchRequest):
    results = search_documents(
        request.query,
        request.top_k
    )

    return {
        "query": request.query,
        "results": results,
    }