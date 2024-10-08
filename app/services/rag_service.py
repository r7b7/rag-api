from app.config import settings
from app.models.clients.embedder import TransformerEmbedder
from app.models.clients.generator import QueryGenerator
from app.db.vector_store import VectorStore
from adalflow.components.model_client import GroqAPIClient
from app.models.clients.summarizer import Summarizer

class RAGService:
    def __init__(
        self,
        embedder: TransformerEmbedder,
        generator: QueryGenerator,
        vector_store: VectorStore,
        summarizer: Summarizer
    ):
        self.embedder = embedder
        self.generator = generator
        self.vector_store = vector_store
        self.summarizer = summarizer

    async def process_query(self, query: str):
        embeddings = self.embedder.get_embeddings(query)
        relevant_docs = self.vector_store.search(embeddings)
        summarized_doc = self.summarizer.summarize(relevant_docs)
        response = self.generator(query + " "+ summarized_doc)
        return response.data.response
    
def get_rag_service():
    generator = QueryGenerator(
        model_client=GroqAPIClient(),
        model_kwargs={"model": settings.GENERATOR_MODEL},
    )
    rag_service =  RAGService(TransformerEmbedder(), generator, VectorStore(), Summarizer())
    return rag_service