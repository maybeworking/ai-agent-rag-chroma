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
https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/

````
documents = load_documents()
print(documents[0])
````

other references on doc loaders:
- https://python.langchain.com/docs/how_to/#document-loaders


How to load: 
- https://python.langchain.com/docs/how_to/document_loader_pdf/

Version migrations: 
I used langchain-cli migrate
https://python.langchain.com/docs/versions/v0_2/

## Ollama

Open-source model: llamma3.2 etc
embeded: mxbai-embed-large

embed-model: https://ollama.com/library/mxbai-embed-large
More about embedding models: https://ollama.com/blog/embedding-models