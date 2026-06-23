# Knowledge base

This folder contains the embedding store used by the RAG pipeline:

- `embeddings_3072.json` — 3,072-dimensional `gemini-embedding-001` vectors for the curated SVET knowledge base. Retrieval at inference time used cosine similarity with threshold 0.30 and top-k = 10.

For this peer-review release, only the embedding store is included. The full curated source documents are retained by the authors and will be addressed in the final archival release after peer review.

The RAG pipeline parameters (embedding model, dimension, similarity metric, threshold, top-k) are described in the Methods section of the manuscript.
