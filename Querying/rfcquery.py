from transformers import AutoTokenizer, AutoModel
import numpy as np
import faiss

# Paths
faiss_index_path = '/home/madhukiran/Desktop/Samsung-Prism/vectorDB/faiss_index.index'
chunk_map_path = '/home/madhukiran/Desktop/Samsung-Prism/vectorDB/chunk_map.json'

# Load the FAISS index
index = faiss.read_index(faiss_index_path)

# Load the chunk map
import json
with open(chunk_map_path, 'r') as file:
    chunk_map = json.load(file)

# Load the tokenizer and model
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def query_vector(query_text):
    inputs = tokenizer(query_text, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

def retrieve_chunks(query_text, top_k=5):
    query_vector = query_vector(query_text)
    distances, indices = index.search(query_vector, top_k)
    
    results = []
    for i in range(top_k):
        idx = indices[0][i]
        chunk = chunk_map.get(str(idx), "Chunk not found")
        results.append((distances[0][i], chunk))
    
    return results

# Example query
query_text = "Explain the key features of the HTTP protocol."
results = retrieve_chunks(query_text)

# Print results
for distance, chunk in results:
    print(f"Distance: {distance}\nChunk: {chunk}\n")
