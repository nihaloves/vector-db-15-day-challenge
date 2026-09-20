# Day 7 — Document Chunking


sentences = [
    "Vector databases store numerical representations of information called embeddings.",
    "Embeddings allow computers to compare the semantic meaning of different pieces of text.",
    "Approximate Nearest Neighbor search makes it possible to search large collections of vectors efficiently.",
    "HNSW is a graph-based indexing algorithm commonly used for approximate nearest neighbor search.",
    "Retrieval-Augmented Generation combines retrieval with language models to provide relevant context for generating answers."
]


def chunk_sentences(sentences, max_characters=200, overlap_sentences=1):
    """
    Create chunks from sentences.

    max_characters:
        Approximate maximum size of each chunk.

    overlap_sentences:
        Number of sentences shared between consecutive chunks.
    """

    chunks = []
    current_chunk = []

    for sentence in sentences:

        candidate = current_chunk + [sentence]
        candidate_text = " ".join(candidate)

        if current_chunk and len(candidate_text) > max_characters:

            # Save the current chunk
            chunks.append(" ".join(current_chunk))

            # Keep the last sentence for overlap
            current_chunk = current_chunk[-overlap_sentences:]

            # Add the new sentence
            current_chunk.append(sentence)

        else:
            current_chunk = candidate

    # Save the final chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


# Create chunks
chunks = chunk_sentences(
    sentences,
    max_characters=200,
    overlap_sentences=1
)


# Display sentences
print("\nSENTENCES:\n")

for i, sentence in enumerate(sentences, start=1):
    print(f"{i}. {sentence}")


# Display chunk information
print(f"\nNumber of sentences: {len(sentences)}")
print(f"Number of chunks: {len(chunks)}")

print("\nChunks:\n")

for i, chunk in enumerate(chunks, start=1):
    print(f"--- Chunk {i} ---")
    print(chunk)
    print()