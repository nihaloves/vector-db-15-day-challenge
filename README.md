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

The later part of the challenge will move into:

* RAG
* retrieval evaluation
* production concepts
* building a final retrieval/RAG project

The exact direction may change as I learn more.

---

## How this repo works

Each day has its own folder containing the code and a small README explaining what I learned.

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

phase-3-rag/
│
├── day-11-rag-foundations/
├── day-12-rag-app/
├── day-13-evaluation/
├── day-14-production-concepts/
└── day-15-final-project/
```

I'm keeping the explanations simple because I want this repository to remain useful to me later, not just serve as documentation for this challenge.

---

## Progress

### Phase 1 — Foundations

* [x] Day 01 — First vector database with ChromaDB
* [x] Day 02 — Understanding embeddings
* [x] Day 03 — Vector similarity
* [x] Day 04 — Working with Qdrant
* [x] Day 05 — Metadata filtering

### Phase 2 — Retrieval & Search

* [x] Day 06 — ANN & HNSW
* [x] Day 07 — Document chunking
* [x] Day 08 — Semantic search
* [x] Day 09 — Hybrid retrieval
* [x] Day 10 — Retrieval pipeline

### Phase 3 — RAG

* [ ] Day 11 — RAG foundations
* [ ] Day 12 — Building a RAG app
* [ ] Day 13 — Retrieval evaluation
* [ ] Day 14 — Production concepts
* [ ] Day 15 — Final project

**10 / 15 days complete.**

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

And a retrieval pipeline turns these individual techniques into a reusable system.

That becomes especially important when building **Retrieval-Augmented Generation (RAG)** systems.

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
