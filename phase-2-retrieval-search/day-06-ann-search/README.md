# Day 6 — ANN & HNSW

## Goal

Understand **Approximate Nearest Neighbor (ANN)** search and how **Qdrant** uses **HNSW** for efficient vector indexing.

---

## What I Learned

### ANN — Approximate Nearest Neighbor

When a vector database contains a large number of vectors, comparing a query vector against every stored vector becomes expensive.

**ANN (Approximate Nearest Neighbor)** search aims to find highly similar vectors efficiently without exhaustively comparing the query against every vector.

The trade-off is that ANN prioritizes **search speed and scalability** over guaranteed exact nearest-neighbor results.

---

### HNSW

**HNSW** stands for **Hierarchical Navigable Small World**.

It is a graph-based indexing algorithm commonly used for approximate nearest-neighbor search.

HNSW organizes vectors into multiple graph layers:

* **Higher layers** allow faster, larger jumps through the graph.
* **Lower layers** provide more detailed navigation.
* The search gradually moves toward vectors that are more similar to the query.

This allows large vector collections to be searched much more efficiently than a simple exhaustive scan.

---

## HNSW Parameters

For this experiment, the Qdrant collection was configured with:

```python
hnsw_config=HnswConfigDiff(
    m=16,
    ef_construct=100,
)
```

### `m`

Controls the connectivity of the HNSW graph, including how many connections are maintained for each vector.

Higher values can improve graph connectivity and recall, but require more memory and construction work.

### `ef_construct`

Controls how much effort is spent while **building** the HNSW graph.

Higher values can produce a better-quality index, but increase index construction cost.

### `ef`

`ef` is a **search-time** parameter.

It controls how much effort is spent while searching the HNSW graph.

### Parameter Summary

| Parameter      | Stage              | Purpose                      |
| -------------- | ------------------ | ---------------------------- |
| `m`            | Index construction | Controls graph connectivity  |
| `ef_construct` | Index construction | Controls construction effort |
| `ef`           | Search             | Controls search effort       |

---

## Experiment

I created an in-memory Qdrant collection containing **10 documents**.

### Configuration

* **Embedding model:** `all-MiniLM-L6-v2`
* **Embedding dimensions:** 384
* **Distance metric:** Cosine similarity
* **Vector database:** Qdrant
* **Index configuration:** HNSW

### Query

```text
I want to learn about artificial intelligence
```

### Top Result

```text
Artificial intelligence allows computers to perform intelligent tasks
```

Similarity score:

```text
0.6178
```

The semantic search returned the most relevant document based on vector similarity rather than exact keyword matching.

---

## Important Observation

Although HNSW was configured, Qdrant reported:

```text
indexed_vectors_count=0
points_count=10
```

The collection also had:

```text
full_scan_threshold=10000
```

Since the collection contained only **10 vectors**, a full scan can be more appropriate than building and using an HNSW index.

This highlights an important practical concept:

> Configuring HNSW does not necessarily mean HNSW will be used for a very small collection.

For larger collections, approximate nearest-neighbor indexing becomes increasingly useful because exhaustive comparison becomes more expensive.

---

## ANN vs Exact Search

### Exact / Brute-Force Search

```text
Query
  ↓
Compare with every vector
  ↓
Rank all results
  ↓
Return nearest vectors
```

This guarantees exact nearest neighbors but becomes expensive as the dataset grows.

### ANN Search

```text
Query
  ↓
Navigate an index
  ↓
Explore promising candidates
  ↓
Return nearest candidates
```

ANN reduces search cost by avoiding an exhaustive comparison with every vector.

---

## Key Takeaways

* **ANN** stands for Approximate Nearest Neighbor.
* ANN is a general approach for efficient similarity search at scale.
* **HNSW** stands for Hierarchical Navigable Small World.
* HNSW is a graph-based indexing algorithm for ANN search.
* `m` controls graph connectivity.
* `ef_construct` controls HNSW construction effort.
* `ef` controls search-time effort.
* Small datasets may use full-scan search because it can be cheaper than ANN indexing.
* ANN becomes increasingly valuable as the number of vectors grows.

---

## Technologies Used

* Python
* Qdrant
* Sentence Transformers
* `all-MiniLM-L6-v2`

---

**Next:** Day 7 — Document Chunking
