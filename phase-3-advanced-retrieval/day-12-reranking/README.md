# Day 12 - Reranking

## Objective

Improve retrieval quality by adding a reranking stage after initial vector retrieval.

The system first retrieves candidate documents using embedding similarity and then uses a cross-encoder to score and reorder those candidates.

---

## Concepts Covered

* Two-stage retrieval
* Candidate retrieval
* Cross-encoder reranking
* Query-document relevance
* Retrieval scores vs reranking scores
* Ranking improvement

---

## How It Works

```text
User Query
    ↓
Embedding Model
    ↓
Initial Retrieval
    ↓
Candidate Documents
    ↓
Cross-Encoder
    ↓
Reranking
    ↓
Final Results
```

The first retrieval stage is designed to find relevant candidates efficiently.

The reranking stage examines each query-document pair more closely and assigns a new relevance score.

---

## Retriever vs Reranker

### Retriever

The retriever uses sentence embeddings to represent the query and documents as vectors.

It then compares those vectors using cosine similarity.

```text
Query → Embedding
Document → Embedding
        ↓
Cosine Similarity
        ↓
Candidate Results
```

This stage is useful for quickly narrowing a large collection down to a smaller set of candidates.

### Reranker

The reranker uses a cross-encoder model.

Instead of independently encoding the query and document, it processes them together:

```text
(Query, Document)
        ↓
Cross-Encoder
        ↓
Relevance Score
```

The candidates are then sorted using these new scores.

---

## Example

The query used in this experiment was:

```text
How can I build an API using Python?
```

### Initial Retrieval

```text
1. FastAPI
   Retrieval Score: 0.6843

2. Python
   Retrieval Score: 0.5275

3. Python 3.13
   Retrieval Score: 0.3754

4. Retrieval augmented generation
   Retrieval Score: 0.1443

5. Java
   Retrieval Score: 0.0936
```

### After Reranking

```text
1. FastAPI
   Rerank Score: 4.0426

2. Python
   Rerank Score: -1.5201

3. Python 3.13
   Rerank Score: -6.0204

4. Java
   Rerank Score: -9.9655

5. Retrieval augmented generation
   Rerank Score: -11.1880
```

The reranker changed the ordering of the final two candidates.

This shows that the ranking produced by the initial retrieval stage does not necessarily have to be the final ranking.

---

## Why Reranking Matters

Vector retrieval is useful for finding candidates quickly, but the initial similarity score is not always enough to determine the best ordering.

Reranking provides a second stage that can examine the relationship between the query and each candidate more closely.

A common retrieval architecture is therefore:

```text
Large Document Collection
        ↓
Fast Retrieval
        ↓
Top-K Candidates
        ↓
Reranking
        ↓
Top Results
```

This approach balances retrieval speed with better ranking quality.

---

## Key Learning

The main lesson from Day 12 is that **retrieval and ranking are separate problems**.

A vector search system can first retrieve a manageable set of potentially relevant documents.

A more computationally expensive reranker can then be applied only to those candidates.

This two-stage approach makes it possible to improve ranking quality without running the more expensive model against the entire document collection.

---

## Run

```powershell
python main.py
```
