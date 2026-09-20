from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue
)
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create in-memory Qdrant
client = QdrantClient(":memory:")


# Create collection
client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)


# Documents
documents = [
    {
        "text": "I love Python programming",
        "language": "python",
        "level": "beginner"
    },
    {
        "text": "Python is useful for data science",
        "language": "python",
        "level": "intermediate"
    },
    {
        "text": "Java is an object oriented programming language",
        "language": "java",
        "level": "beginner"
    },
    {
        "text": "Java uses classes and objects",
        "language": "java",
        "level": "intermediate"
    },
    {
        "text": "Machine learning uses data to make predictions",
        "language": "python",
        "level": "advanced"
    }
]


# Create embeddings
texts = [document["text"] for document in documents]
embeddings = model.encode(texts).tolist()


# Create Qdrant points
points = []

for i, (document, embedding) in enumerate(zip(documents, embeddings)):
    points.append(
        PointStruct(
            id=i,
            vector=embedding,
            payload=document
        )
    )


# Store points
client.upsert(
    collection_name="documents",
    points=points
)


print(f"Stored {len(points)} documents.")


# Query
query = "I want to learn programming"
query_embedding = model.encode(query).tolist()


# Search only Python documents
results = client.query_points(
    collection_name="documents",
    query=query_embedding,
    query_filter=Filter(
        must=[
            FieldCondition(
                key="language",
                match=MatchValue(value="python")
            )
        ]
    ),
    limit=3
)


print("\nQuery:")
print(query)

print("\nPython documents only:")

for result in results.points:
    print(
        f"Score: {result.score:.4f} | "
        f"Language: {result.payload['language']} | "
        f"Level: {result.payload['level']} | "
        f"Text: {result.payload['text']}"
    )