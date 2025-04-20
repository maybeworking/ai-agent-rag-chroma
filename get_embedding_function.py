from langchain_ollama.embeddings import OllamaEmbeddings

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="mxbai-embed-large:latest") 
    return embeddings