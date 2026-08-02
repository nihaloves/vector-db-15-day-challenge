# Day 02 — Understanding Embeddings

Yesterday, I used ChromaDB to perform my first semantic search.

But there was something I didn't really understand:

**What exactly happens to the text before it reaches the vector database?**

Today I went one step backwards and looked at embeddings.

---

## What is an embedding?

An embedding is a numerical representation of some data.

For text, an embedding model takes a sentence and converts it into a vector (basically a list of numbers).

For example:

```text
"I love dogs."
      ↓
Embedding Model
      ↓
[0.0041, -0.0193, 0.1151, ...]
```

In today's experiment, I used:

```text
all-MiniLM-L6-v2
```

and each sentence was converted into a vector with **384 dimensions**.

So:

```text
"I love dogs."
      ↓
[384 numbers]
```

---

## What do those 384 numbers mean?

This was one of my biggest questions today.

At first, it is tempting to think that each number represents something specific:

```text
dimension 1 → animals
dimension 2 → emotion
dimension 3 → dogs
...
```

But it doesn't work that way.

The information is distributed across the whole vector.

The complete vector represents a location in a high-dimensional space.

We can't directly visualize 384 dimensions, but we can compare the positions of different vectors.

---

## Why are embeddings useful?

Consider these sentences:

```text
"I love dogs."

"I adore puppies."

"My favorite animal is a dog."
```

They use different words, but they have related meanings.

An embedding model tries to represent these relationships in its vector space.

This allows us to compare sentences based on their representations rather than only looking for exact keyword matches.

That's the basic idea behind **semantic similarity**.

---

# What I experimented with

I generated embeddings for these five sentences:

```text
1. I love dogs.
2. I adore puppies.
3. I enjoy programming.
4. The database uses an index.
5. I made pasta for dinner.
```

The model produced:

```text
Embedding dimensions: 384
```

I then compared every sentence with every other sentence using cosine similarity.

The resulting similarity matrix was:

```text
tensor([
    [ 1.0000,  0.6892,  0.3877,  0.0520,  0.1985],
    [ 0.6892,  1.0000,  0.2870, -0.0388,  0.1880],
    [ 0.3877,  0.2870,  1.0000,  0.1157,  0.2427],
    [ 0.0520, -0.0388,  0.1157,  1.0000,  0.0377],
    [ 0.1985,  0.1880,  0.2427,  0.0377,  1.0000]
])
```

The most interesting comparison was:

```text
"I love dogs."
vs.
"I adore puppies."

Similarity: 0.6892
```

while:

```text
"I love dogs."
vs.
"The database uses an index."

Similarity: 0.0520
```

The model was able to represent the dog-related sentences as more similar than the unrelated ones.

---

## Something unexpected

I also tried:

```text
"Apple released a new phone."
vs.
"Apple is a fruit."
```

and got:

```text
Similarity: 0.4542
```

This was interesting because the sentences have different meanings, but they share the word "Apple".

It reminded me that embeddings aren't a perfect representation of human understanding.

They capture patterns learned from language, and the results can sometimes be surprising.

---

## Understanding the similarity matrix

The diagonal contains `1.0000`:

```text
dog        → dog        = 1.0000
puppy      → puppy      = 1.0000
programming → programming = 1.0000
...
```

That makes sense because every sentence is perfectly similar to itself.

The other values show how similar the different sentence vectors are according to cosine similarity.

For example:

```text
Dog ↔ Puppy          0.6892
Dog ↔ Programming    0.3877
Dog ↔ Database       0.0520
```

The important thing isn't to interpret `0.6892` as "68.92% similar".

It is a similarity score, and its meaning depends on the model, representation, and metric.

---

## The pipeline I'm understanding

Today I connected another piece to yesterday's experiment:

```text
                TEXT
                  ↓
           Embedding Model
                  ↓
        384-dimensional Vector
                  ↓
          Similarity Measure
                  ↓
           Similarity Score
```

And eventually:

```text
                 DOCUMENTS
                     ↓
              Embedding Model
                     ↓
                  Vectors
                     ↓
               Vector DB
                     ↓
                   Query
                     ↓
              Similarity Search
                     ↓
              Relevant Results
```

---

## What I learned

* An embedding is a vector representation of data.
* My embedding model produces 384-dimensional vectors.
* The individual dimensions aren't simple human-readable concepts.
* The complete vector represents a position in a high-dimensional space.
* Similarity can be measured between embeddings.
* Semantic similarity doesn't necessarily require exact keyword matches.
* Embeddings aren't perfect representations of meaning.

---

## Questions I'm taking into Day 03

I now understand that we're comparing vectors.

But...

**How exactly are we comparing them?**

What does a similarity score actually calculate?

And what's the difference between:

* Cosine similarity
* Euclidean distance
* Dot product

That's what I'm exploring next.

---

**Day 02/15 ✅**
