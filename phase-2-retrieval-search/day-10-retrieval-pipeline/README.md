# Day 10 — Retrieval Pipeline

## Goal

Build a reusable retrieval pipeline that combines semantic search and keyword search to retrieve relevant documents.

## What I learned

A retrieval pipeline connects different search techniques into a single workflow.

The pipeline built in this exercise is:

```text
Query
  ↓
Semantic Retrieval
  +
Keyword Retrieval
  ↓
Keyword Score Normalization
  ↓
Hybrid Score
  ↓
Rank Results
  ↓
Top Documents
```

## Semantic Retrieval

Semantic retrieval converts the query into an embedding and searches for documents with similar embeddings.

This allows the system to find documents based on meaning rather than only exact words.

In this project, SentenceTransformers generates embeddings and Qdrant performs vector search using cosine similarity.

## Keyword Retrieval

Keyword retrieval checks whether the words in the query appear in each document.

The implementation uses case-insensitive whole-word matching with Python regular expressions.

Documents containing more query words receive higher keyword scores.

## Score Normalization

Keyword scores are normalized so that they can be combined with semantic similarity scores.

```text
normalized keyword score = keyword score / maximum keyword score
```

## Hybrid Retrieval

The final score combines both retrieval methods:

```text
hybrid score =
    0.5 × keyword score
    +
    0.5 × semantic score
```

This gives equal weight to exact keyword matching and semantic similarity.

## Example

Query:

```text
Python 3.13
```

The pipeline returned:

```text
1. Python 3.13 introduced several improvements...
   Hybrid Score: 0.8658

2. Python is a popular programming language...
   Hybrid Score: 0.4266

3. Retrieval augmented generation combines...
   Hybrid Score: 0.0231
```

The first document receives the highest score because it contains the exact query terms and is also semantically similar to the query.

## Why Hybrid Retrieval?

Semantic search is useful for understanding meaning, but it can sometimes miss the importance of exact terms.

Keyword search is useful when exact words, names, versions, identifiers, or technical terms matter.

Combining both approaches can make retrieval more robust.

## Technologies

* Python
* SentenceTransformers
* Qdrant
* Regular expressions
* Cosine similarity

## Simplified Implementation

This project is an educational implementation of hybrid retrieval.

The current pipeline only combines keyword scores with the documents returned by the top semantic results. Production retrieval systems may use larger candidate sets, more advanced ranking methods such as Reciprocal Rank Fusion (RRF), tuned weights, and evaluation datasets.

## Key Takeaway

A retrieval pipeline turns individual search techniques into a reusable system.

This is an important step toward Retrieval-Augmented Generation (RAG), where the retrieved documents can later be passed to a language model as context.
