# Day 7 — Document Chunking

## Overview

Today I learned how documents are divided into smaller pieces called **chunks** before being stored and retrieved from a vector database.

Chunking is an important step in Retrieval-Augmented Generation (RAG) because embedding an entire large document as one vector can make retrieval less precise.

---

## What I Learned

### 1. What is a chunk?

A chunk is a smaller piece of a larger document.

For example:

```text
Large Document
      ↓
Sentence 1
Sentence 2
Sentence 3
Sentence 4
Sentence 5
      ↓
Smaller chunks
```

Instead of embedding the entire document as one vector, we can create embeddings for smaller sections.

---

### 2. Why do we need chunking?

Large documents can contain many different topics.

If the entire document is converted into one embedding, a search query may retrieve the document even when only a small part of it is relevant.

Chunking allows the retrieval system to find a more specific piece of information.

```text
Document
   ↓
Chunks
   ↓
Embeddings
   ↓
Vector Database
   ↓
Semantic Search
   ↓
Relevant Chunks
```

---

## 3. Sentence-based chunking

For this exercise, the document was represented as individual sentences.

The sentences were then grouped into chunks with a maximum target size of approximately **200 characters**.

The implementation does not split a sentence in the middle.

This keeps the chunks more readable and preserves sentence boundaries.

---

## 4. Chunk overlap

The implementation uses **one-sentence overlap**.

For example:

```text
Chunk 1:
Sentence 1 + Sentence 2

Chunk 2:
Sentence 2 + Sentence 3

Chunk 3:
Sentence 3 + Sentence 4

Chunk 4:
Sentence 4 + Sentence 5
```

The repeated sentence provides context between neighboring chunks.

Without overlap:

```text
Chunk 1 → Sentence 1 + 2
Chunk 2 → Sentence 3 + 4
```

A piece of context near the boundary could become separated.

With overlap:

```text
Chunk 1 → Sentence 1 + 2
                 ↓
Chunk 2 → Sentence 2 + 3
```

Sentence 2 connects the two chunks.

---

## 5. Important parameters

### `max_characters`

Controls the approximate maximum size of a chunk.

```python
max_characters=200
```

This is a simple character-based limit used for this exercise.

Real-world systems often use token-based chunk sizes instead.

### `overlap_sentences`

Controls how many sentences are carried from one chunk into the next.

```python
overlap_sentences=1
```

---

## 6. Result

Input:

```text
5 sentences
```

Output:

```text
4 chunks
```

with one sentence of overlap between consecutive chunks.

---

## Key Takeaway

Chunking is not just about cutting text into arbitrary pieces.

A good chunk should:

* contain meaningful information
* preserve context
* avoid unnecessary fragmentation
* be small enough for effective retrieval
* work well with the embedding model

Chunking quality directly affects the quality of semantic search and RAG.

---

## Next Step

**Day 8 — Semantic Search Engine**

The next step is to take these chunks, convert them into embeddings, store them in a vector database, and retrieve the most semantically relevant chunks for a query.
