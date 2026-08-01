import chromadb

# Create a persistent local Chroma database
client = chromadb.PersistentClient(
    path="./chroma_db"
)

# Create a collection
collection = client.get_or_create_collection(
    name="tech_notes"
)

# Add documents
collection.add(
    documents=[
        "Vector databases store embeddings for similarity search.",
        "PostgreSQL can perform vector search using pgvector.",
        "Python is widely used for software development.",
        "HNSW is an algorithm used for approximate nearest neighbor search.",
        "Sourdough bread requires flour, water, and a starter."
    ],
    ids=[
        "doc1",
        "doc2",
        "doc3",
        "doc4",
        "doc5"
    ]
)

print("Documents stored:", collection.count())

# Search using natural language
query = "How can I store embeddings for AI applications?"

results = collection.query(
    query_texts=[query],
    n_results=3
)

print("\nQuery:", query)
print("\nResults:")

for i, document in enumerate(results["documents"][0]):
    print(f"\n{i + 1}. {document}")

    print("\nCollection contents:")

data = collection.get(
    include=["documents", "embeddings"]
)

print("IDs:", data["ids"])
print("Number of embeddings:", len(data["embeddings"]))