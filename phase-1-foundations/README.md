# Phase 1 — Foundations

## Overview

Phase 1 focuses on understanding the fundamental ideas behind vector databases and semantic search.

The goal was not just to use a vector database, but to understand the pipeline:

```text
Text
 ↓
Embedding
 ↓
Vector
 ↓
Vector Database
 ↓
Similarity Search
 ↓
Filtered Retrieval
```

By the end of this phase, I built semantic search experiments using both **ChromaDB** and **Qdrant**.

---

## Days

### Day 1 — First Vector Database

**Focus:** ChromaDB

Learned how to:

* Create a vector database
* Store documents
* Generate embeddings
* Perform a similarity search
* Retrieve semantically related documents

---

### Day 2 — Text Embeddings

**Focus:** Converting text into vectors

Learned:

* What embeddings are
* Why machines represent text as vectors
* How similar meanings produce similar vector representations
* How `Sentence Transformers` generate embeddings

Model used:

`all-MiniLM-L6-v2`

---

### Day 3 — Vector Similarity

**Focus:** Comparing vectors

Learned:

* Vector similarity
* Cosine similarity
* Similarity scores
* Semantic search

Instead of matching exact words, the system can retrieve text based on meaning.

---

### Day 4 — Qdrant

**Focus:** Working with a dedicated vector database

Built a semantic search system using:

* Qdrant
* `qdrant-client`
* Sentence Transformers
* 384-dimensional embeddings

Learned about:

* Collections
* Vectors
* Points
* Payloads
* Vector search

---

### Day 5 — Metadata Filtering

**Focus:** Combining vector search with structured constraints

Learned how Qdrant payloads can be used to filter search results.

For example:

```text
Query
  ↓
Semantic similarity
  +
Metadata filter
  ↓
Relevant results
```

This allows applications to search semantically while restricting results based on metadata such as:

* Language
* Category
* User
* Date
* Level
* Tags

---

## Phase 1 Architecture

The concepts learned in this phase fit together like this:

```text
                 DOCUMENT
                     │
                     ▼
            Sentence Transformer
                     │
                     ▼
               EMBEDDING
                     │
                     ▼
              VECTOR DATABASE
                ┌────┴────┐
                │         │
             Vector     Payload
                │         │
                └────┬────┘
                     ▼
                   QUERY
                     │
                     ▼
               Similarity Search
                     │
                     +
              Metadata Filter
                     │
                     ▼
              Relevant Results
```

---

## Technologies

* Python
* ChromaDB
* Qdrant
* qdrant-client
* Sentence Transformers
* `all-MiniLM-L6-v2`

---

## Key Takeaways

### 1. Text can be represented as vectors

Embedding models convert text into numerical representations that capture semantic information.

### 2. Vector databases store and search embeddings

Instead of searching only for matching words, vector databases can search for similar meanings.

### 3. Similarity metrics determine how vectors are compared

This phase used **cosine similarity**.

### 4. Metadata adds structure to semantic search

Vector similarity alone is not always enough. Metadata filters allow applications to combine semantic retrieval with structured conditions.

---

## Phase 1 Outcome

By completing Phase 1, I can now build a basic semantic search system from scratch:

```text
Text
→ Embedding
→ Vector storage
→ Similarity search
→ Metadata filtering
→ Relevant results
```

The next phase moves beyond individual experiments into **retrieval systems and real document search**.

---

## Next

**Phase 2 — Retrieval & Search**
