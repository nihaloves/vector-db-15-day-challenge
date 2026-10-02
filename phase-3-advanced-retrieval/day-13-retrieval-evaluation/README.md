# Day 13 - Retrieval Evaluation

## Objective

Measure the quality of the retrieval system using evaluation metrics instead of relying only on manually inspecting search results.

The system evaluates whether relevant documents are being retrieved and how highly they are ranked.

---

## Concepts Covered

* Retrieval evaluation
* Ground-truth evaluation data
* Precision@K
* Recall@K
* Reciprocal Rank
* Mean Reciprocal Rank (MRR)
* Retrieval quality measurement

---

## Evaluation Pipeline

```text
Evaluation Query
        ↓
Vector Retrieval
        ↓
Top-K Results
        ↓
Compare with Relevant Documents
        ↓
Calculate Evaluation Metrics
```

The evaluation dataset contains queries and the topics considered relevant to each query.

---

## Evaluation Metrics

### Precision@K

Precision@K measures how many of the top-K retrieved documents are relevant.

```text
Precision@K =
Relevant Results in Top-K
-------------------------
          K
```

For example, if 2 out of the top 3 results are relevant:

```text
Precision@3 = 2 / 3 = 0.6667
```

---

### Recall@K

Recall@K measures how many of the relevant documents available in the collection were retrieved within the top-K results.

```text
Recall@K =
Relevant Results Retrieved
--------------------------
Total Relevant Documents
```

A higher recall means the system is finding more of the relevant documents.

---

### Reciprocal Rank

Reciprocal Rank measures the position of the first relevant result.

```text
Position 1 → 1.0
Position 2 → 0.5
Position 3 → 0.333
```

If the first relevant result is ranked first, the reciprocal rank is 1.0.

---

### Mean Reciprocal Rank

MRR is the average reciprocal rank across all evaluation queries.

```text
MRR =
Sum of Reciprocal Ranks
----------------------
Number of Queries
```

---

## Evaluation Results

Three queries were evaluated.

### Query 1

```text
How can I build an API using Python?
```

```text
1. FastAPI
   Score: 0.6843

2. Python
   Score: 0.5275

3. Python 3.13
   Score: 0.3754
```

```text
Precision@3:     1.0000
Recall@3:        1.0000
Reciprocal Rank: 1.0000
```

---

### Query 2

```text
What is a vector database?
```

```text
1. Vector databases
   Score: 0.6447

2. Java
   Score: 0.2241

3. Retrieval augmented generation
   Score: 0.1584
```

```text
Precision@3:     0.3333
Recall@3:        1.0000
Reciprocal Rank: 1.0000
```

---

### Query 3

```text
What is retrieval augmented generation?
```

```text
1. Retrieval augmented generation
   Score: 0.7183

2. Vector databases
   Score: 0.2116

3. Python 3.13
   Score: 0.1333
```

```text
Precision@3:     0.3333
Recall@3:        1.0000
Reciprocal Rank: 1.0000
```

---

## Overall Results

```text
Mean Precision@3: 0.5556
Mean Recall@3:    1.0000
MRR:              1.0000
```

The evaluation shows that the system consistently retrieves a relevant result at the top of the ranking.

Recall@3 is 1.0000 because all relevant documents in the evaluation collection were retrieved within the top three results.

Precision@3 is lower because some of the remaining top-three results were not relevant to the query.

MRR is 1.0000 because the first relevant result was ranked first for every evaluation query.

---

## Key Learning

The main lesson from Day 13 is that retrieval quality should be measured quantitatively.

A retrieval system may appear good when inspecting a few results manually, but evaluation metrics provide a more systematic way to understand its behavior.

Different metrics measure different aspects of retrieval:

```text
Precision → How many retrieved results are relevant?
Recall    → How many relevant results were found?
MRR       → How highly is the first relevant result ranked?
```

These metrics can later be used to compare different retrieval strategies and improvements.

---

## Run

```powershell
python main.py
```
