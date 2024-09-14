import os
from sentence_transformers import SentenceTransformer
import numpy as np

# Load pre-trained model from Sentence-Transformers
model = SentenceTransformer('all-MiniLM-L6-v2')

# Directory where the chunks are stored
chunks_dir = '/home/madhukiran/Desktop/Samsung-Prism/chunking/chunks'

# Function to load a chunk file
def load_chunk(chunk_file):
    with open(chunk_file, 'r') as file:
        return file.read()

# List all chunk files in the directory
chunk_files = sorted([os.path.join(chunks_dir, file) for file in os.listdir(chunks_dir) if file.startswith('chunk_')])

# Generate embeddings for all chunks and store them
embeddings = []
for chunk_file in chunk_files:
    chunk = load_chunk(chunk_file)
    chunk_embedding = model.encode(chunk, show_progress_bar=True)
    embeddings.append(chunk_embedding)

# Convert list of embeddings to numpy array
embeddings = np.array(embeddings)

# Save the embeddings to a file
np.save('/home/madhukiran/Desktop/Samsung-Prism/embedding/embeddings.npy', embeddings)

print("Embeddings successfully generated and saved.")
