import chromadb

class VectorStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("olympics_wiki_collection")
        
    def search(self, query_embedding):
        retrieved_embedding= self.collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=1,
            include=["documents"]
        )
        retrieved_doc = retrieved_embedding['documents'][0][0]
        return retrieved_doc
    
    def save(self, text_array, embedding_array):
        self.collection.add(
            embeddings= [embedding for embedding in embedding_array],
            documents=[para for para in text_array],
            ids=[f"{i}" for i in range(len(text_array)) ]
        )