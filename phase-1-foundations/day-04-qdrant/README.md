# Day 4 — Qdrant

## What I learned

Today I moved from ChromaDB to **Qdrant**, a vector database for storing and searching high-dimensional vectors.

### Concepts

- Qdrant collections
- Vectors and vector dimensions
- Points and payloads
- Cosine similarity
- Semantic search
- Storing real embeddings in Qdrant
- Querying Qdrant using an embedding

## How it works

```text
Text
 ↓
Sentence Transformer
 ↓
384-dimensional embedding
 ↓
Qdrant
 ↓
Cosine similarity
 ↓
Most similar documents