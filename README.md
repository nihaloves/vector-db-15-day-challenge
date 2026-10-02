# Vector DB — 15 Day Challenge

I'm a second-year Computer Science student, and I recently realized I knew almost nothing about vector databases.

So I decided to change that.

This is my **15-day learning challenge to understand vector databases by actually working with them** — writing code, breaking things, debugging, experimenting, and documenting what I learn along the way.

This isn't a "build 15 projects in 15 days" challenge.

The goal is to **understand the concepts properly**.

---

## What I'm learning

So far, I've worked with:

* embeddings
* vector similarity
* ChromaDB
* Qdrant
* metadata filtering
* ANN search
* HNSW
* document chunking
* semantic search
* keyword search
* hybrid retrieval
* retrieval pipelines
* metadata-aware retrieval

The later part of the challenge will move into:

* reranking
* retrieval evaluation
* search APIs
* production concepts
* RAG
* building a final retrieval/RAG project

The exact direction may change as I learn more.

---

## How this repo works

Each day has its own folder containing the code and a small README explaining what I learned along the way.

The challenge is divided into three phases:

```text
phase-1-foundations/
│
├── day-01-first-vector-db/
├── day-02-embeddings/
├── day-03-vector-similarity/
├── day-04-qdrant/
└── day-05-metadata-filtering/

phase-2-retrieval-search/
│
├── day-06-ann-search/
├── day-07-document-chunking/
├── day-08-semantic-search/
├── day-09-hybrid-retrieval/
└── day-10-retrieval-pipeline/

phase-3-advanced-retrieval/
│
├── day-11-metadata-retrieval/
├── day-12-reranking/
├── day-13-retrieval-evaluation/
├── day-14-search-api/
└── day-15-final-project/
```

I'm keeping the explanations simple because I want this repository to remain useful to me later, not just serve as documentation for this challenge.

---

## Progress

### Phase 1 — Foundations

* Day 01 — First vector database with ChromaDB
* Day 02 — Understanding embeddings
* Day 03 — Vector similarity
* Day 04 — Working with Qdrant
* Day 05 — Metadata filtering

### Phase 2 — Retrieval & Search

* Day 06 — ANN & HNSW
* Day 07 — Document chunking
* Day 08 — Semantic search
* Day 09 — Hybrid retrieval
* Day 10 — Retrieval pipeline

### Phase 3 — Advanced Retrieval

* Day 11 — Metadata-aware retrieval
* Day 12 — Reranking
* Day 13 — Retrieval evaluation
* Day 14 — Search API
* Day 15 — Final retrieval/RAG project

**11 / 15 days complete.**

---

## What I've understood so far

One thing I've realized during this challenge is that a vector database isn't just about storing vectors.

The interesting part is the whole retrieval process:

```text
Document
   ↓
Embedding
   ↓
Vector Database
   ↓
Query
   ↓
Filtering
   ↓
Retrieval
   ↓
Ranking
   ↓
Relevant Context
```

I've also started seeing how different retrieval techniques solve different problems.

Semantic search helps retrieve information based on meaning.

Keyword search helps when exact terms matter.

Hybrid retrieval combines both.

Metadata filtering adds structured constraints to the search.

And a retrieval pipeline brings these individual techniques together into a reusable system.

Day 11 took this further by combining **metadata filtering with semantic similarity**, allowing the search process to first restrict the available documents and then rank the matching results by similarity.

The next part of the challenge will explore how retrieved results can be **reranked, evaluated, and exposed through an API**, before bringing the pieces together into a final system.

---

## Why I'm doing this

I came across vector databases and realized that I understood very little about what was happening underneath the AI applications using them.

I could have just watched tutorials and copied a RAG application.

Instead, I wanted to go one layer deeper.

So I'm learning the pieces individually, testing them with small programs, and trying to understand **why** each piece exists before putting everything together.

There have already been plenty of moments where something didn't work exactly as expected.

Those moments are part of the challenge too.

This repository is my learning trail rather than a collection of polished projects.

If you're learning vector databases too, feel free to follow along.

**15 days. One concept at a time.**
