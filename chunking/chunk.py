# Create a virtual environment
#python -m venv rag_env

# Activate the virtual environment
# On Windows:
#rag_env\Scripts\activate
# On macOS/Linux:
#source rag_env/bin/activate

# Upgrade pip
#pip install --upgrade pip


#Install Necessary Libraries



import nltk
from nltk.tokenize import sent_tokenize

# Specify custom download directory
nltk.data.path.append('./rag_env/nltk_data')
# Download the Punkt tokenizer for sentence splitting
nltk.download('punkt', download_dir='./rag_env/nltk_data')
nltk.download('punkt_tab', download_dir='./rag_env/nltk_data')

file_path = '/home/madhukiran/Desktop/Samsung-Prism/Data/RFC_3261/rfc3261.txt'


def load_text(path):
    with open(path, 'r') as file:
        text = file.read()
    return text.strip()

# Function to create chunks from tokenized sentences
def create_chunks(sentences, max_chunk_size=1000):
    chunks = []
    current_chunk = []
    current_size = 0

    for sentence in sentences:
        sentence_size = len(sentence)
        if current_size + sentence_size <= max_chunk_size:
            current_chunk.append(sentence)
            current_size += sentence_size
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
            current_size = sentence_size

    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

# Function to save chunks into separate text files
def save_chunks(chunks, output_dir='chunks'):
    import os
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i, chunk in enumerate(chunks):
        with open(f'{output_dir}/chunk_{i+1}.txt', 'w') as chunk_file:
            chunk_file.write(chunk)


# Load the RFC 3261 document
rfc_text = load_text(file_path)

# Tokenize the text into sentences
sentences = sent_tokenize(rfc_text)

# Create chunks of the tokenized sentences
chunks = create_chunks(sentences, max_chunk_size=1000)

# Save the chunks to files (optional)
save_chunks(chunks)

# Check the first 3 chunks
for i, chunk in enumerate(chunks[:3]):
    print(f"Chunk {i+1}:\n{chunk}\n")