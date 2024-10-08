import unittest
from unittest.mock import MagicMock, patch
from app.services.document_service import DocumentService

class TestDocumentService(unittest.TestCase):

    @patch('app.services.document_service.pdfplumber.open') 
    @patch('app.services.document_service.tempfile.NamedTemporaryFile') 
    def test_process_document(self, mock_tempfile, mock_pdf_open):
            mock_vector_store = MagicMock()
            mock_embedder = MagicMock()        
            mock_sentence_splitter = MagicMock()    
         
            document_service = DocumentService(mock_vector_store, mock_embedder, mock_sentence_splitter)
            file_content = b"Fake PDF content"
            document_service.process_document(file_content)

            mock_vector_store.save.assert_called_once()
            mock_sentence_splitter.split_text_to_chunks.assert_called_once()

          
if __name__ == '__main__':
    unittest.main()