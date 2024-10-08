# RAG - API
This is a work in progress, Latest version is merged to main branch but older versions are accessible in appropriately named branches.

# Installation
1. pip install pdfplumber
2. pip install tf-keras
3. pip install groq
4. pip install adalflow
5. pip install transformers
6. pip install pydantic-settings
7. pip install -U pytest

# Run application
Run the application using the below command

```python3.12 -m uvicorn app.main:app --reload```

# OpenAPI Specification (Former Swagger)
1. Access specification at http://127.0.0.1:8000/api/v1/openapi.json


# Access Endpoints
1. Access the APIs using these endpoints 
 - Health Check - http://127.0.0.1:8000/api/v1/health/
 
 - Document Upload - http://127.0.0.1:8000/api/v1/documents/upload

 ``` curl --location 'http://127.0.0.1:8000/api/v1/documents/upload' --form 'file=@"<add_file_path>"' ``` 

 - Rag - http://127.0.0.1:8000/api/v1/rag/query 
 ``` curl --location 'http://127.0.0.1:8000/api/v1/rag/query' --header 'Content-Type: application/json' --data '{"text":"Who won 2024 olympics"}' ```


# Run unit tests

Set PYTHONPATH before running tests
### Linux/Mac
export PYTHONPATH=$PYTHONPATH:$(pwd)

### Windows PowerShell
$env:PYTHONPATH = "$env:PYTHONPATH;$(pwd)"

Then run tests
### Run all tests 
pytest 
### Run with coverage 
pytest --cov=app 
### Run specific test file 
pytest tests/unit/api/v1/endpoints/test_healthcheck.py 
### Run with verbose output 
pytest -v