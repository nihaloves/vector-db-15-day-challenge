from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer


# 1. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Create Qdrant in memory
client = QdrantClient(":memory:")


# 3. Create collection
client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)


# 4. Our documents
documents = [
    "I love Python programming",
    "Java is an object oriented programming language",
    "The weather is beautiful today",
    "Machine learning uses data to make predictions",
    "I enjoy building software"
]


# 5. Convert documents into embeddings
embeddings = model.encode(documents).tolist()


# 6. Create Qdrant points
points = []

for i, (document, embedding) in enumerate(zip(documents, embeddings)):
    points.append(
        PointStruct(
            id=i,
            vector=embedding,
            payload={"text": document}
        )
    )


# 7. Store the points
client.upsert(
    collection_name="documents",
    points=points
)


print(f"Stored {len(points)} documents in Qdrant.")


# 8. Create a query
query = "I want to learn programming"

query_embedding = model.encode(query).tolist()


# 9. Search Qdrant
results = client.query_points(
    collection_name="documents",
    query=query_embedding,
    limit=3
)


# 10. Display results
print("\nQuery:")
print(query)

print("\nMost similar documents:")

for result in results.points:
    print(
        f"Score: {result.score:.4f} | "
        f"Text: {result.payload['text']}"
    )