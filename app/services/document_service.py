from app.db.vector_store import VectorStore
import pdfplumber
import tempfile

from app.models.clients.embedder import TransformerEmbedder


class DocumentService:
    def __init__(self, vector_store: VectorStore, embedder: TransformerEmbedder):
        self.vector_store = vector_store
        self.embedder = embedder
        
    def process_document(self,content):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(content)
            temp_file_path = temp_file.name
        text_array = []
        with pdfplumber.open(temp_file_path) as pdf:
            for page in pdf.pages:
                text_array.append(page.extract_text())
        embeddings_array = [self.embedder.get_embeddings(para).tolist() for para in text_array]
        self.vector_store.save(text_array, embeddings_array)
        
def get_document_service():
    doc_service = DocumentService(VectorStore(), TransformerEmbedder())
    return doc_service