# ai-agent-rag-chroma

1. pip install -r requirements.txt
2. Store data in chroma db
````python populate_database.py ````
3. Create embeddings
4. Create vector store
5. Create a retriever
6. Create a chain
7. Ask questions


# References
## langchain: 

Documents:
https://python.langchain.com/docs/how_to/#document-loaders

````
documents = load_documents()
print(documents[0])
````
How to load: 
- https://python.langchain.com/docs/integrations/document_loaders/

Version migrations: 
I used langchain-cli migrate
https://python.langchain.com/docs/versions/v0_2/

## Langchain & Ollama utalized

Langchain: https://python.langchain.com/docs/integrations/text_embedding/ollama/
Embedding models: https://ollama.com/blog/embedding-models
embed-model: https://ollama.com/library/mxbai-embed-large

Langchain: https://python.langchain.com/docs/integrations/chat/ollama/
Ollama: https://ollama.com/
Open-source model: https://ollama.com/library/gemma2
 