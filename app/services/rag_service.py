from app.config import settings
from app.models.clients.embedder import TransformerEmbedder
from app.models.clients.generator import QueryGenerator
from app.db.vector_store import VectorStore
from adalflow.components.model_client import GroqAPIClient

class RAGService:
    def __init__(
        self,
        embedder: TransformerEmbedder,
        generator: QueryGenerator,
        vector_store: VectorStore
    ):
        self.embedder = embedder
        self.generator = generator
        self.vector_store = vector_store

    async def process_query(self, query: str):
        embeddings = self.embedder.get_embeddings(query)
        relevant_docs = self.vector_store.search(embeddings)
        response = self.generator(query + " "+ relevant_docs)
        return response.data.response
    
def get_rag_service():
    generator = QueryGenerator(
        model_client=GroqAPIClient(),
        model_kwargs={"model": settings.GENERATOR_MODEL},
    )
    rag_service =  RAGService(TransformerEmbedder(), generator, VectorStore())
    return rag_service