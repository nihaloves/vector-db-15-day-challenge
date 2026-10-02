# Day 11 - Metadata-Aware Retrieval

## Objective

Extend semantic search by combining vector similarity with metadata filtering.

The system first filters documents using metadata and then ranks the matching documents using cosine similarity.

## Concepts Covered

- Metadata filtering
- Semantic similarity
- Cosine similarity
- Top-K retrieval
- Multiple metadata conditions
- Filtered vector search

## How It Works

```text
User Query
    ↓
Metadata Filters
    ↓
Matching Documents
    ↓
Generate Embeddings
    ↓
Cosine Similarity
    ↓
Sort by Similarity
    ↓
Top-K Results