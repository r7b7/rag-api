import unittest
from unittest.mock import MagicMock

from app.services.rag_service import RAGService

class TestRagService(unittest.TestCase):

    def test_process_query(self):
        mock_vector_store = MagicMock()
        mock_embedder = MagicMock()         
        mock_generator = MagicMock() 

        rag_service = RAGService(mock_embedder,mock_generator, mock_vector_store)
        rag_service.process_query("test query")

if __name__ == '__main__':
    unittest.main()