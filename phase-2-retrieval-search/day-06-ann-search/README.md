# Day 6 — ANN & HNSW

## Goal

Understand Approximate Nearest Neighbor (ANN) search and how Qdrant uses HNSW for vector indexing.

## What I Learned

### ANN — Approximate Nearest Neighbor

When a vector database contains a very large number of vectors, comparing a query vector against every stored vector becomes expensive.

ANN search aims to find very similar vectors efficiently without performing an exhaustive comparison against every vector.

### HNSW

HNSW stands for **Hierarchical Navigable Small World**.

It is a graph-based indexing algorithm used for efficient approximate nearest neighbor search.

The graph contains multiple layers:

- Higher layers allow larger jumps through the graph.
- Lower layers provide more detailed navigation.
- The search moves through the graph toward vectors that are increasingly similar to the query.

### HNSW Parameters

Qdrant was configured with:

```python
m=16
ef_construct=100

m

Controls the connectivity of the HNSW graph, including the number of connections maintained for vectors.

Higher values can improve connectivity and recall, but require more memory and construction work.

ef_construct

Controls how much effort is spent while constructing the HNSW graph.

Higher values can produce a better-quality index but increase construction cost.

ef

ef is a search-time parameter.

It controls how much effort is spent while searching the HNSW graph.

So:

Parameter	Stage	Purpose
m	Index construction	Graph connectivity
ef_construct	Index construction	Index construction effort
ef	Search	Search effort
Experiment

I stored 10 documents in an in-memory Qdrant collection using:

all-MiniLM-L6-v2
384-dimensional embeddings
Cosine similarity
HNSW configuration

Query:

I want to learn about artificial intelligence

Top result:

Artificial intelligence allows computers to perform intelligent tasks

with a similarity score of approximately 0.6178.

Important Observation

Although HNSW was configured, Qdrant reported:

indexed_vectors_count=0
points_count=10

The collection also had:

full_scan_threshold=10000

Since the collection contains only 10 vectors, Qdrant can use a full scan instead of building an HNSW index.

This demonstrates an important practical point:

Configuring an HNSW index does not necessarily mean HNSW will be used for a very small collection.

For larger collections, ANN indexing becomes much more useful.

Key Takeaways

ANN is a general approach for efficient approximate nearest-neighbor search.
HNSW is a graph-based ANN indexing algorithm.
m controls graph connectivity.
ef_construct controls index construction effort.
ef controls search-time effort.
Small datasets may use exact/full-scan search because it can be cheaper than ANN indexing.