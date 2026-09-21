# Day 8 — Semantic Search Engine

## Objective

Build a simple semantic search engine that converts documents and a user query into vector embeddings, stores the document embeddings in Qdrant, and retrieves the most semantically relevant documents.

## How It Works

The search pipeline is:

```text
Documents
    ↓
Text Embeddings
    ↓
Qdrant Vector Database
    ↓
User Query
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Top Relevant Results
```

## Technologies

* Python
* Sentence Transformers
* `all-MiniLM-L6-v2`
* Qdrant
* Cosine similarity

## Implementation

Five example documents are converted into embeddings using:

```python
SentenceTransformer("all-MiniLM-L6-v2")
```

The model generates a **384-dimensional vector** for each document.

These vectors are stored in an in-memory Qdrant collection using cosine similarity.

The query:

```text
How can I search information using vectors?
```

is also converted into a 384-dimensional embedding.

Qdrant then compares the query vector with the stored document vectors and returns the top 3 results.

## Example Output

```text
QUERY:
How can I search information using vectors?

TOP RESULTS:

1. Score: 0.5656
   Vector databases store embeddings and enable semantic search.

2. Score: 0.3223
   HNSW is an algorithm used for approximate nearest neighbor search.

3. Score: 0.3205
   Retrieval augmented generation combines search with language models.
```

## What I Learned

### Keyword Search vs Semantic Search

Keyword search primarily looks for matching words.

Semantic search represents text as vectors and compares their meaning using vector similarity. This allows related text to be retrieved even when the exact words in the query and document are different.

For example:

```text
Query:
How can I search information using vectors?

Result:
Vector databases store embeddings and enable semantic search.
```

The query and result do not contain exactly the same wording, but their meanings are related.

### Embeddings

An embedding is a numerical representation of text.

Similar meanings tend to produce vectors that are closer together in the embedding space.

### Vector Database

Qdrant stores the document vectors and performs similarity search against the query vector.

### Cosine Similarity

Cosine similarity measures how similar two vectors are based on the angle between them.

A higher similarity score indicates that the vectors are more closely aligned.

## Key Takeaway

Semantic search changes the retrieval process from:

```text
"Do these texts contain similar words?"
```

to:

```text
"Do these texts have similar meanings?"
```

This forms an important foundation for later retrieval pipelines and RAG systems.
