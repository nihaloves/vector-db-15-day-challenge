# Day 01 — My First Vector Database

I started this challenge because I wanted to understand what vector databases actually are and why they're becoming important in AI applications.

Before today, I had heard of databases like MySQL, PostgreSQL and MongoDB, but vector databases were completely new to me.

So I decided to start by actually using one.

---

## First: What is a vector database?

A normal database is good at storing structured information.

For example:

```text
id: 101
name: Niharika
course: CSE
year: 2
```

But AI applications often need to work with things like:

* text
* images
* documents
* audio
* user preferences

These can be represented as **vectors**, lists of numbers that capture patterns or meaning.

A vector database is designed to store these vectors and efficiently find vectors that are similar to one another.

That's what makes it useful for things like:

* semantic search
* recommendation systems
* RAG
* AI assistants
* document retrieval
* similarity search

---

## What is semantic search?

This was the first concept I wanted to understand.

Imagine I have a document containing:

> "Vector databases store high-dimensional embeddings for similarity search."

If I search:

> "How can I store embeddings for AI applications?"

A traditional keyword search might struggle because the words aren't exactly the same.

Semantic search instead tries to understand the **meaning** of the query and find information with a similar meaning.

The basic idea is:

```text
Document
   ↓
Embedding
   ↓
Vector
   ↓
Vector Database

Query
   ↓
Embedding
   ↓
Vector
   ↓
Find similar vectors
   ↓
Relevant results
```

---

# What I used

For my first experiment, I used:

* Python
* ChromaDB
* A local persistent vector database

I created a collection called:

```text
tech_topics
```

and added five documents covering different topics.

For example:

```text
Vector databases store embeddings for similarity search.

PostgreSQL can perform vector search using pgvector.

Python is widely used for software development.

HNSW is an approximate nearest neighbor graph algorithm.

Baking sourdough bread requires a healthy starter, flour, water, and patience.
```

I also added metadata to each document, such as:

```text
category
level
```

---

## My first semantic query

I asked:

```text
How can I store embeddings for AI applications?
```

ChromaDB returned:

```text
1. Vector databases store embeddings for similarity search.

2. PostgreSQL can perform vector search using pgvector.

3. Python is widely used for software development.
```

The interesting part was that I didn't tell the database to look specifically for the word "embeddings".

It compared the query with the stored representations and returned what it considered relevant.

---

## What I noticed

The first result was obviously the most relevant:

```text
Vector databases store embeddings for similarity search.
```

The PostgreSQL result also made sense because `pgvector` is related to storing and searching vectors.

But the Python result was less relevant.

That was actually useful to see.

It showed me that **semantic search isn't magic**.

A vector database returns results based on similarity, and the quality of those results depends on things like:

* the embedding model
* the data
* the similarity metric
* the query
* the retrieval settings

---

# What is actually stored?

One thing I wanted to understand was what happens to the text.

The database doesn't simply store:

```text
"I love dogs."
```

and somehow "understand" it.

The text is converted into a numerical representation called an **embedding**.

Conceptually:

```text
"I love dogs."
      ↓
Embedding model
      ↓
[0.02, -0.14, 0.31, ...]
      ↓
Vector
```

Those vectors can then be compared.

I didn't fully understand embeddings yet when I started Day 1.

So that's exactly what I'm exploring on **Day 2**.

---

## What I learned today

My main takeaways:

1. Vector databases are databases designed for vector data and similarity search.
2. Semantic search is different from traditional keyword search.
3. Text can be converted into numerical vectors called embeddings.
4. Similar vectors can be retrieved from a vector database.
5. Metadata can be stored alongside vectors.
6. ChromaDB makes it possible to experiment with vector search locally.

---

## The part I still don't understand

This is probably the most important part of this challenge.

I can now use a vector database.

But I don't want to just memorize:

```python
collection.query(...)
```

I want to understand what is actually happening underneath.

So my next questions are:

**What exactly is an embedding?**

**Why does a sentence become hundreds of numbers?**

**How does the database decide that two vectors are similar?**

That's what I'm exploring next.

---

### Progress

**Day 01 / 15 — Completed ✅**

Next:

**Day 02 — Understanding Embeddings**
