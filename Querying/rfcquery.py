import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Directory where the chunks are stored
chunks_dir = r'Samsung-Prism\chunking\chunks'

# Load the precomputed embeddings
embeddings_path = r'Samsung-Prism\embedding\embeddings.npy'
embeddings = np.load(embeddings_path)

# Function to load a chunk file
def load_chunk(chunk_file):
    with open(chunk_file, 'r') as file:
        return file.read()

# List all chunk files in the directory
chunk_files = sorted([os.path.join(chunks_dir, file) for file in os.listdir(chunks_dir) if file.startswith('chunk_')])

# Function to handle the query and find the most relevant chunks
def query_chunks(query, top_k=5):
    # Encode the query using the same model
    query_embedding = model.encode(query)

    # Compute cosine similarity between query and all precomputed chunk embeddings
    similarities = cosine_similarity([query_embedding], embeddings)[0]

    # Get the indices of the top_k most similar chunks
    top_k_indices = np.argsort(similarities)[-top_k:][::-1]

    # Retrieve the corresponding chunks and their similarity scores
    top_chunks = []
    for idx in top_k_indices:
        chunk_file = chunk_files[idx]
        chunk_text = load_chunk(chunk_file)
        similarity_score = similarities[idx]
        top_chunks.append((chunk_text, similarity_score))

    return top_chunks

# Example usage:
if __name__ == '__main__':
    query = "Explain Stateless Proxy"
    top_chunks = query_chunks(query, top_k=5)

    # Display the top results
    print("\nTop relevant chunks:\n")
    for i, (chunk, score) in enumerate(top_chunks):
        print(f"Chunk {i+1} (Similarity: {score:.4f}):\n{chunk}\n")

