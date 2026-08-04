# Day 3 — Vector Similarity

## Objective

Understand how vectors are compared and how similarity metrics can be used to build a basic semantic search system.

This experiment explores three common ways of comparing vectors:

* Cosine Similarity
* Euclidean Distance
* Dot Product

It then applies cosine similarity to real text embeddings to perform semantic search.

---

## What I Learned

An embedding represents text as a numerical vector.

Once text has been converted into vectors, we can compare those vectors mathematically to determine how closely related they are.

The basic pipeline is:

```text
Text
 ↓
Embedding Model
 ↓
Vector
 ↓
Similarity Calculation
 ↓
Ranking
 ↓
Top-K Results
```

---

## 1. Cosine Similarity

Cosine similarity measures how similarly two vectors are oriented.

* Higher value → more similar
* Lower value → less similar

For this experiment:

```text
A = [1, 2, 3]
B = [1, 2, 3]
C = [3, 2, 1]

A vs B = 1.0
A vs C = 0.7143
```

Since A and B are identical, their cosine similarity is 1.

---

## 2. Euclidean Distance

Euclidean distance measures the distance between two vectors.

* Smaller distance → more similar
* Larger distance → less similar

Results:

```text
A vs B = 0.0
A vs C = 2.8284
```

A and B are identical, so their distance is zero.

---

## 3. Dot Product

The dot product measures the alignment between two vectors.

Results:

```text
A vs B = 14
A vs C = 10
```

A higher value indicates stronger alignment in this experiment.

---

# Semantic Search Experiment

After testing basic vectors, I used the `all-MiniLM-L6-v2` embedding model to convert five sentences into 384-dimensional vectors.

### Query

```text
I want to learn programming.
```

### Documents

```text
1. Python is a popular programming language.
2. I love learning how to code.
3. The beach was beautiful today.
4. Machine learning uses data to make predictions.
5. I enjoy playing football with my friends.
```

The query was converted into an embedding and compared with every document embedding using cosine similarity.

---

## Results

```text
0.6051 → I love learning how to code.
0.5308 → Python is a popular programming language.
0.1836 → I enjoy playing football with my friends.
0.1821 → Machine learning uses data to make predictions.
-0.0446 → The beach was beautiful today.
```

The results were then sorted by similarity, allowing the system to return the **Top 3** most similar results.

### Top 3

```text
1. I love learning how to code.
2. Python is a popular programming language.
3. I enjoy playing football with my friends.
```

---

## Important Observation

The similarity score should not be interpreted as a percentage.

For example:

```text
0.6051 ≠ 60.51% semantic similarity
```

The score is useful primarily for comparing and ranking vectors within the search.

The experiment also showed that embedding models are not perfect. A small dataset can sometimes produce surprising rankings, which is why real retrieval systems need evaluation using representative data.

---

## Key Takeaways

* Embeddings convert text into numerical vectors.
* Similarity metrics allow vectors to be compared.
* Cosine similarity focuses on the orientation of vectors.
* Euclidean distance measures the distance between vectors.
* Dot product measures vector alignment.
* Semantic search can rank documents based on meaning rather than exact keyword matching.
* Top-K retrieval returns only the highest-ranked results.
* Embedding models provide useful representations, but their results are not always perfect.

---

## Technologies Used

* Python
* NumPy
* Sentence Transformers
* `all-MiniLM-L6-v2`

---

## Next

**Day 4 — Introduction to Qdrant**

The next step is to move from manually comparing vectors to storing and searching vectors inside an actual vector database.
