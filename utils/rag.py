from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def split_text(text, chunk_size=500):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(words[i:i + chunk_size])

        chunks.append(chunk)

    return chunks


def build_index(text):

    chunks = split_text(text)

    embeddings = model.encode(chunks)

    index = faiss.IndexFlatL2(
        embeddings.shape[1]
    )

    index.add(
        np.array(embeddings).astype("float32")
    )

    return index, chunks


def search(index, chunks, query, top_k=3):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        top_k
    )

    return [
        chunks[i]
        for i in indices[0]
    ]