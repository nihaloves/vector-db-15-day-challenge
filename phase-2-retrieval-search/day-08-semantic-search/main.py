# Day 8 — Semantic Search Engine

from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Create an in-memory Qdrant database
client = QdrantClient(":memory:")

collection_name = "semantic_search"


# Create collection
client.create_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)


# Documents to search
documents = [
    "Python is a popular programming language used for software development.",
    "Machine learning allows computers to learn patterns from data.",
    "Vector databases store embeddings and enable semantic search.",
    "HNSW is an algorithm used for approximate nearest neighbor search.",
    "Retrieval augmented generation combines search with language models.",
]


# Convert documents into embeddings
embeddings = model.encode(documents)


# Store documents and embeddings
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


# Search query
query = "How can I search information using vectors?"

query_embedding = model.encode(query)


# Perform semantic search
results = client.query_points(
    collection_name=collection_name,
    query=query_embedding.tolist(),
    limit=3
).points


print("\nQUERY:")
print(query)

print("\nTOP RESULTS:\n")

for i, result in enumerate(results, start=1):
    print(f"{i}. Score: {result.score:.4f}")
    print(f"   {result.payload['text']}")
    print()