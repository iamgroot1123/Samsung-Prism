import numpy as np
import faiss
import json
from sentence_transformers import SentenceTransformer

# Load the pre-trained model for query embedding
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAISS index
index = faiss.read_index('Samsung-Prism/vectorDB/faiss_index.index')

# Load chunk map (to retrieve the text associated with embeddings)
with open('Samsung-Prism/vectorDB/chunk_map.json', 'r') as f:
    chunk_map = json.load(f)

# Function to handle the query and find the most relevant chunks
def query_chunks_faiss(query, top_k=5):
    # Step 1: Encode the query into an embedding
    query_embedding = model.encode(query)

    # Step 2: Reshape query_embedding to match FAISS input requirements (1, embedding_dimension)
    query_embedding = np.expand_dims(query_embedding, axis=0)

    # Step 3: Search the FAISS index for the top_k most similar embeddings (using L2 distance)
    distances, indices = index.search(query_embedding, top_k)

    # Step 4: Retrieve the top-k chunks based on FAISS results
    top_chunks = []
    for i in range(top_k):
        chunk_id = indices[0][i]  # Get the chunk index
        similarity_score = distances[0][i]  # Get the L2 distance (lower is better)
        chunk_text = chunk_map[str(chunk_id)]  # Retrieve the corresponding chunk text
        top_chunks.append((chunk_text, similarity_score))

    return top_chunks

# Example usage
if __name__ == '__main__':
    query = "Explain Stateless Proxy."
    top_chunks = query_chunks_faiss(query, top_k=5)

    # Display the top results
    print("\nTop relevant chunks:\n")
    for i, (chunk, score) in enumerate(top_chunks):
        print(f"Chunk {i+1} (L2 Distance: {score:.4f}):\n{chunk}\n")
