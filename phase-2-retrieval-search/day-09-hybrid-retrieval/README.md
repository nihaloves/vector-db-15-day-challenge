# Day 9 — Hybrid Retrieval

## Objective

Combine **keyword search** and **semantic search** to improve retrieval.

---

## What is Hybrid Retrieval?

Hybrid retrieval combines two different search approaches:

* **Keyword retrieval** finds documents containing exact query terms.
* **Semantic retrieval** finds documents based on meaning using embeddings.

Combining both allows a system to use the strengths of each approach.

For example, a query such as:

```text
Python 3.13
```

benefits from keyword matching because the exact version `3.13` is important, while semantic search can find documents that discuss related Python concepts.

---

## 1. Keyword Retrieval

The keyword search checks whether the words in the query appear in each document.

For the query:

```text
Python 3.13
```

the document:

```text
Python 3.13 introduced several improvements to the Python programming language.
```

gets a higher keyword score because it contains both query terms.

---

## 2. Semantic Retrieval

Semantic search uses the `all-MiniLM-L6-v2` embedding model to convert documents and queries into vectors.

The vectors are stored in Qdrant and compared using cosine similarity.

This allows the system to retrieve documents based on meaning rather than exact words.

---

## 3. Score Normalization

Keyword scores and semantic similarity scores are on different scales, so they should not be combined directly.

The keyword scores are normalized using the maximum keyword score:

```text
normalized score = keyword score / maximum keyword score
```

This produces keyword scores between `0` and `1`.

---

## 4. Hybrid Score

The implementation combines the normalized keyword score and semantic score equally:

```text
hybrid score = 0.5 × keyword score + 0.5 × semantic score
```

The documents are then sorted by their hybrid score.

For example:

```text
Keyword Score: 1.0000
Semantic Score: 0.7316

Hybrid Score:
0.5 × 1.0000 + 0.5 × 0.7316
= 0.8658
```

---

## Example Output

For the query:

```text
Python 3.13
```

the highest-ranked document was:

```text
Python 3.13 introduced several improvements to the Python programming language.
```

with a hybrid score of approximately:

```text
0.8658
```

This document ranked highly because it matched the exact keywords and was also semantically similar to the query.

---

## Key Takeaway

Hybrid retrieval combines:

```text
Keyword Search
      +
Semantic Search
      ↓
Hybrid Ranking
```

Keyword search is useful when exact terms matter, while semantic search is useful when meaning matters.

Together, they can provide more flexible retrieval than either approach alone.

> Note: This is a simplified educational implementation. Production retrieval systems may use more advanced ranking and fusion techniques and tune the weights based on evaluation results.
