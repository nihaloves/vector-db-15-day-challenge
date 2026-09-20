# Day 5 — Metadata Filtering

## What I learned

Today I learned how vector search can be combined with **metadata filtering**.

Vector similarity finds semantically similar documents, while metadata filters allow us to control which documents are considered during the search.

## Concepts

* Qdrant payloads
* Metadata
* Metadata filtering
* `Filter`
* `FieldCondition`
* `MatchValue`
* Combining filtering with vector similarity

## How it works

```text
Query
  ↓
Embedding model
  ↓
Query vector
  ↓
Metadata filter
  ↓
Matching documents
  ↓
Vector similarity
  ↓
Ranked results
```

## Example

The database contains both Python and Java documents.

The query was:

`I want to learn programming`

Without a filter, Qdrant could return semantically similar documents from either language.

For this experiment, I added:

```python
Filter(
    must=[
        FieldCondition(
            key="language",
            match=MatchValue(value="python")
        )
    ]
)
```

This tells Qdrant to only search documents whose payload contains:

```text
language = python
```

The returned results were therefore all Python documents.

## Why this matters

Real applications often need more than semantic similarity.

For example:

* Search only documents from a particular category
* Search only products under a certain price
* Search only articles from a particular year
* Search only content belonging to a specific user
* Search only documents with a particular tag

Metadata filtering allows vector search to be combined with these constraints.

## Key takeaway

**Vector similarity answers:**

> "What is semantically similar?"

**Metadata filtering answers:**

> "What am I allowed to search?"

Combining both makes vector search much more useful in real applications.

## Stack

* Python
* Qdrant
* qdrant-client
* Sentence Transformers
* all-MiniLM-L6-v2
