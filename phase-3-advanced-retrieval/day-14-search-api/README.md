# Day 14 - Search API

## Objective

Expose the semantic retrieval system through a REST API using FastAPI.

The API accepts a search query, performs vector-based retrieval, ranks the documents using cosine similarity, and returns the results as JSON.

---

## Concepts Covered

* FastAPI
* REST API
* POST endpoints
* Request validation with Pydantic
* Semantic search
* Vector embeddings
* Cosine similarity
* JSON responses
* API documentation with Swagger UI

---

## How It Works

```text
Client
  ↓
POST /search
  ↓
FastAPI
  ↓
Query Embedding
  ↓
Cosine Similarity
  ↓
Rank Documents
  ↓
Top-K Results
  ↓
JSON Response
```

---

## API Endpoint

### `POST /search`

The endpoint accepts a search query and the number of results to return.

Example request:

```json
{
  "query": "How can I build an API using Python?",
  "top_k": 3
}
```

Example response:

```json
{
  "query": "How can I build an API using Python?",
  "results": [
    {
      "text": "FastAPI is a Python framework for building APIs.",
      "score": 0.6843
    },
    {
      "text": "Python is a popular programming language used for software development.",
      "score": 0.5275
    },
    {
      "text": "Python 3.13 introduced several improvements to the Python programming language.",
      "score": 0.3754
    }
  ]
}
```

---

## Request Validation

The API uses Pydantic to validate incoming requests.

```python
class SearchRequest(BaseModel):
    query: str
    top_k: int = Field(default=3, ge=1, le=6)
```

This limits `top_k` to values between 1 and 6 because the current document collection contains six documents.

Invalid values are rejected by the API instead of being processed.

---

## API Documentation

FastAPI automatically provides interactive API documentation.

The documentation can be accessed at:

```text
http://127.0.0.1:8000/docs
```

This allows the `/search` endpoint to be tested directly from the browser.

---

## Example Retrieval

For the query:

```text
How can I build an API using Python?
```

the API returned:

```text
1. FastAPI
   Score: 0.6843

2. Python
   Score: 0.5275

3. Python 3.13
   Score: 0.3754
```

The results match the retrieval behavior observed in the earlier experiments.

---

## Key Learning

The main lesson from Day 14 is that a retrieval system can be exposed as a reusable API.

Instead of running the retrieval code directly, another application can send an HTTP request to the `/search` endpoint and receive ranked results in JSON format.

This creates a foundation for integrating retrieval into larger applications.

---

## Run

Start the API server with:

```powershell
python -m uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

and test the `/search` endpoint.
