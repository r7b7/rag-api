# RAG - API
This is a work in progress, Latest version is merged to main branch but older versions are accessible in appropriately named branches.

# Installation
1. pip install pdfplumber
2. pip install tf-keras
3. pip install groq
4. pip install adalflow
5. pip install transformers
6. pip install pydantic-settings

# Run application
Run the application using the below command

```python3.12 -m uvicorn app.main:app --reload```

# OpenAPI Specification (Former Swagger)
1. Access specification at http://127.0.0.1:8000/api/v1/openapi.json


# Access Endpoints
1. Access the APIs using these endpoints 
 1.1 Health Check - http://127.0.0.1:8000/api/v1/health/
 1.2 Document Upload - http://127.0.0.1:8000/api/v1/documents/upload
 1.3 Rag - http://127.0.0.1:8000/api/v1/rag/query 



