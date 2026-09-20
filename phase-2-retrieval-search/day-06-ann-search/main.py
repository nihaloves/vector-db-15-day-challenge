from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
    HnswConfigDiff,
)
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create in-memory Qdrant
client = QdrantClient(":memory:")


# Create a collection with HNSW configuration
client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE,
        hnsw_config=HnswConfigDiff(
            m=16,
            ef_construct=100,
        ),
    ),
)


# Documents
documents = [
    "Python is a popular programming language",
    "Java is an object oriented programming language",
    "Machine learning uses data to make predictions",
    "Deep learning uses neural networks",
    "Vector databases store embeddings",
    "Semantic search finds information by meaning",
    "Web development uses HTML CSS and JavaScript",
    "Data science involves statistics and programming",
    "Artificial intelligence allows computers to perform intelligent tasks",
    "Software engineering involves designing and maintaining software",
]


# Create embeddings
embeddings = model.encode(documents).tolist()


# Create Qdrant points
points = []

for i, (document, embedding) in enumerate(zip(documents, embeddings)):
    points.append(
        PointStruct(
            id=i,
            vector=embedding,
            payload={
                "text": document
            },
        )
    )


# Store vectors
client.upsert(
    collection_name="documents",
    points=points,
)


print(f"Stored {len(points)} documents.")


# Query
query = "I want to learn about artificial intelligence"
query_embedding = model.encode(query).tolist()


# Search
results = client.query_points(
    collection_name="documents",
    query=query_embedding,
    limit=5,
)


print("\nQuery:")
print(query)

print("\nNearest documents:")

for result in results.points:
    print(
        f"Score: {result.score:.4f} | "
        f"{result.payload['text']}"
    )


# Inspect collection configuration
collection_info = client.get_collection("documents")

print("\nCollection information:")
print(collection_info)