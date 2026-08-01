# Day 1 — Introduction to Vector Databases

If you're completely new to vector databases, this is where I'm starting too.

I'm learning vector databases by building small experiments every day, and I'm documenting what I understand along the way.

The goal of this repository isn't just to collect code. I want it to eventually be something that **someone who knows nothing about vector databases can use to learn them from scratch.**

---

## So, what is a vector database?

Let's start with a normal database.

A traditional database is really good at storing and retrieving structured information.

For example:

```text
Students

ID     Name        Department
01     Niharika    CSE
02     Alex        ECE
03     Maya        CSE
```

If I ask:

> "Find all CSE students"

a normal database can handle that very easily.

But what if I have thousands of documents, images, audio files, or other unstructured data and I want to search them based on **meaning**?

That's where vector databases become useful.

---

## But what's a vector?

A vector is essentially a list of numbers.

For example:

```text
[0.2, 0.8, -0.1, 0.5]
```

This list of numbers can represent some piece of information.

In machine learning, we can transform things like text, images, or audio into these numerical representations.

These representations are called **embeddings**.

For example:

```text
"Dog"
   ↓
Embedding model
   ↓
[0.21, -0.43, 0.76, ...]
```

The actual vectors used by embedding models can have hundreds or thousands of dimensions.

---

## Okay, but why turn text into numbers?

Because numbers give us a way to compare things mathematically.

Imagine we have:

```text
"I love dogs."

"Golden retrievers are adorable."

"I like programming."
```

The first two sentences are related in meaning.

An embedding model tries to represent that relationship in the resulting vectors.

So conceptually:

```text
"I love dogs."              ●
                             \
                              \  close together
                               \
"Golden retrievers..."       ●


"I like programming."                         ●
```

The closer two vectors are in vector space, the more similar they can be according to the chosen similarity measure.

This is the basic idea behind **semantic search**.

---

## What is semantic search?

A normal keyword search might look for exact words.

For example:

```text
Query:
"How can I store embeddings?"
```

A keyword search mainly looks for matching terms such as:

```text
store
embeddings
```

Semantic search instead converts the query into a vector and looks for vectors that are mathematically similar.

So:

```text
Query
  ↓
Embedding
  ↓
Query Vector
  ↓
Compare with stored vectors
  ↓
Find similar vectors
  ↓
Return relevant content
```

This means the result doesn't necessarily need to contain the exact words from the query.

---

## So where does the vector database come in?

A vector database is designed to store and retrieve these vector representations efficiently.

A simplified picture looks like:

```text
                 DOCUMENTS
                     ↓
              Embedding Model
                     ↓
                   Vectors
                     ↓
              ┌─────────────┐
              │ Vector DB   │
              └──────┬──────┘
                     │
                   Search
                     ↓
             Similar Vectors
                     ↓
               Relevant Data
```

A vector database can also store information associated with each vector, such as:

```text
Vector
   +
ID
   +
Original text
   +
Metadata
```

This allows us to retrieve the original information after finding the relevant vectors.

---

# Some terms I learned today

### Vector

A numerical representation represented as a list of numbers.

```text
[0.12, -0.43, 0.71, ...]
```

### Embedding

A vector representation generated from some data using an embedding model.

For example:

```text
Text → Embedding Model → Vector
```

### Vector Database

A database designed to store and search vector representations efficiently.

### Semantic Search

Searching based on the meaning or semantic relationship between the query and stored information rather than relying only on exact keyword matches.

### Similarity

A way of measuring how close or related two vectors are.

I'll be learning more about how this is actually calculated in the upcoming days.

---

# What I did today

Now that I had the basic idea, I wanted to actually use a vector database.

I chose **ChromaDB** for my first experiment.

I created a small collection containing five documents:

```text
1. Vector databases
2. PostgreSQL + pgvector
3. Python
4. HNSW
5. Sourdough baking
```

Then I ran a semantic query:

```text
"How can I store embeddings for AI applications?"
```

The results were:

```text
1. Vector databases store embeddings for similarity search.

2. PostgreSQL can perform vector search using pgvector.

3. Python is widely used for software development.
```

The first result made sense because it was closely related to the meaning of my query.

The interesting part was that I didn't manually tell Chroma which document was relevant.

---

# What was happening behind the scenes?

I originally gave Chroma plain text:

```text
"Vector databases store embeddings for similarity search."
```

Chroma used an embedding model to convert the text into a vector.

Conceptually:

```text
Text
 ↓
Embedding Model
 ↓
[0.12, -0.43, 0.78, ...]
 ↓
ChromaDB
```

My query went through a similar process:

```text
"How can I store embeddings for AI applications?"
                    ↓
              Embedding Model
                    ↓
              Query Vector
                    ↓
             Similarity Search
                    ↓
               Top Results
```

I also inspected the collection and confirmed that the five documents had been converted into five embeddings.

---

# What I still don't understand

This is probably the most important section for me.

I don't want to pretend I understand everything just because the code works.

Right now, I still want to understand:

* How does an embedding model actually generate these numbers?
* What do the individual dimensions of an embedding represent?
* How is similarity between two vectors calculated?
* What exactly does "distance" mean?
* How does a vector database search efficiently when there are millions of vectors?
* What are things like HNSW and ANN actually doing?
* Why use a vector database instead of PostgreSQL or another traditional database?

Those questions are basically going to shape the next few days of this challenge.

---

# Day 1 Takeaway

The biggest thing I understood today is that the basic idea is surprisingly simple:

```text
Data
 ↓
Embedding
 ↓
Vector
 ↓
Store
 ↓
Search by similarity
```

The difficult part is everything underneath that simple-looking pipeline.

And that's what I want to understand next.

---

## What's next?

**Day 2 — Embeddings**

I'll go one level deeper and look at the actual vectors generated from text.

Instead of just using:

```python
collection.query(...)
```

I want to understand what is happening **before the query reaches the database.**

---

### Progress

* [x] Day 01 — Introduction & First ChromaDB Experiment
* [ ] Day 02 — Embeddings
* [ ] Day 03 — Similarity & Distance
* [ ] Day 04 — Qdrant
* [ ] Day 05 — Semantic Search
* [ ] Day 06 — ANN & HNSW
* [ ] Day 07 — Metadata Filtering
* [ ] Day 08 — Hybrid Search
* [ ] Day 09 — Quantization
* [ ] Day 10 — pgvector
* [ ] Day 11 — Chunking
* [ ] Day 12 — RAG
* [ ] Day 13 — Evaluation
* [ ] Day 14 — Capstone
* [ ] Day 15 — Showcase
