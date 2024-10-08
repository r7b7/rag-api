from app.db.vector_store import VectorStore
import pdfplumber
import tempfile

from app.models.clients.embedder import TransformerEmbedder
from app.models.sentence_splitter import SentenceSplitter


class DocumentService:
    def __init__(self, vector_store: VectorStore, embedder: TransformerEmbedder, splitter: SentenceSplitter):
        self.vector_store = vector_store
        self.embedder = embedder
        self.splitter = splitter
        
    def process_document(self,content):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(content)
            temp_file_path = temp_file.name
        extracted_text = []
        with pdfplumber.open(temp_file_path) as pdf:
            for page in pdf.pages:
                extracted_text.append(page.extract_text())

        final_pdf_content = ' '.join(extracted_text)
        text_chunks = self.splitter.split_text_to_chunks(final_pdf_content)

        embeddings_array = [self.embedder.get_embeddings(chunk).tolist() for chunk in text_chunks]
        self.vector_store.save(text_chunks, embeddings_array)
        
def get_document_service():
    doc_service = DocumentService(VectorStore(), TransformerEmbedder(), SentenceSplitter())
    return doc_service
