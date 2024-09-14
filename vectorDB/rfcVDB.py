import numpy as np
import os
import faiss
import json

# Load embeddings
embeddings = np.load('/home/madhukiran/Desktop/Samsung-Prism/embedding/embeddings.npy')

chunk_directory = '/home/madhukiran/Desktop/Samsung-Prism/chunking/chunks'
chunks = []

# Read all chunks into a list in order
for chunk_file in sorted(os.listdir(chunk_directory)):
    with open(os.path.join(chunk_directory, chunk_file), 'r') as f:
        chunks.append(f.read())
        
# Map Embeddings to Chunks
embedding_chunk_mapping = [{'embedding': embeddings[i], 'chunk': chunks[i]} for i in range(len(embeddings))]

# Initialize FAISS index
embedding_dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(embedding_dimension)

# Add embeddings to FAISS index
index.add(embeddings)
print(f"Number of vectors in the index: {index.ntotal}")

# Store chunk metadata separately for retrieval later
chunk_map = {i: chunks[i] for i in range(len(chunks))}

# Save FAISS index
faiss.write_index(index, '/home/madhukiran/Desktop/Samsung-Prism/vectorDB/faiss_index.index')

# Save chunk map as a JSON file
with open('/home/madhukiran/Desktop/Samsung-Prism/vectorDB/chunk_map.json', 'w') as f:
    json.dump(chunk_map, f)

# Load FAISS index
index = faiss.read_index('/home/madhukiran/Desktop/Samsung-Prism/vectorDB/faiss_index.index')
