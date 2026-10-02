# Day 15 - Final Retrieval Project

## Objective

Build a complete semantic retrieval system by combining the main concepts learned throughout the 15-day challenge.

The final project combines:

* Metadata filtering
* Vector retrieval
* Cross-encoder reranking
* FastAPI
* Retrieval evaluation

---

## Architecture

```text
User Query
    ↓
Metadata Filter
    ↓
Vector Retrieval
    ↓
Top-K Candidates
    ↓
Cross-Encoder Reranking
    ↓
Final Ranked Results
```

The system can be accessed through a REST API.

---

## Components

### 1. Metadata Filtering

Documents contain metadata such as:

```text
topic
type
```

A topic filter can be supplied with the search request.

For example:

```json
{
  "query": "What is a vector database?",
  "top_k": 3,
  "topic": "python"
}
```

When a topic filter is provided, documents belonging to other topics are excluded before retrieval.

---

### 2. Vector Retrieval

The system uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

The query and documents are converted into embeddings.

Cosine similarity is then used to calculate the similarity between the query and each document.

```text
Query
  ↓
Embedding
  ↓
Cosine Similarity
  ↓
Candidate Documents
```

---

### 3. Cross-Encoder Reranking

The retrieved candidates are passed to:

```text
cross-encoder/ms-marco-MiniLM-L-6-v2
```

The cross-encoder examines the query and document together and produces a relevance score.

```text
(Query, Document)
        ↓
Cross-Encoder
        ↓
Rerank Score
```

The candidates are then sorted using the reranking scores.

---

## API

The project is implemented using FastAPI.

### Root Endpoint

```text
GET /
```

Returns:

```json
{
  "message": "Advanced Semantic Search API is running"
}
```

### Search Endpoint

```text
POST /search
```

Example request:

```json
{
  "query": "How can I build an API using Python?",
  "top_k": 3
}
```

The response contains:

* Retrieved document text
* Topic
* Document type
* Retrieval score
* Rerank score

### Evaluation Endpoint

```text
GET /evaluate
```

This endpoint runs the evaluation dataset through the retrieval and reranking pipeline.

---

## Evaluation

The evaluation dataset contains three queries:

```text
1. How can I build an API using Python?
2. What is a vector database?
3. What is retrieval augmented generation?
```

The evaluation checks the rank of the first relevant result and calculates Reciprocal Rank.

### Evaluation Results

```text
Query: How can I build an API using Python?
First Relevant Rank: 1
Reciprocal Rank: 1

Query: What is a vector database?
First Relevant Rank: 1
Reciprocal Rank: 1

Query: What is retrieval augmented generation?
First Relevant Rank: 1
Reciprocal Rank: 1
```

### Mean Reciprocal Rank

```text
MRR = 1.0
```

All three evaluation queries returned a relevant document at rank 1 after reranking.

---

## Example Search

Query:

```text
How can I build an API using Python?
```

The system retrieved:

```text
1. FastAPI is a Python framework for building APIs.
2. Python is a popular programming language used for software development.
3. Python 3.13 introduced several improvements to the Python programming language.
```

The FastAPI document received the highest reranking score.

---

## Technologies Used

* Python
* FastAPI
* Pydantic
* Sentence Transformers
* Cross-Encoder
* Cosine Similarity
* Uvicorn

---

## Run the Project

From this directory:

```powershell
python -m uvicorn main:app --reload
```

Open the API documentation at:

```text
http://127.0.0.1:8000/docs
```

The interactive Swagger UI can be used to test the endpoints.

---

## Key Learning

The main lesson from the final project is that a retrieval system can be built as a multi-stage pipeline.

Instead of relying on a single similarity search step, the system combines:

```text
Metadata Filtering
       ↓
Vector Retrieval
       ↓
Reranking
       ↓
Evaluation
       ↓
API
```

Each stage solves a different part of the retrieval problem.

This project brings together the concepts learned throughout the 15-day vector database and retrieval challenge.

---

## Challenge Complete

```text
15 / 15 Days Completed
```

The project now represents the complete learning progression from basic vector concepts to an API-based advanced retrieval system.
