# RAG - API

This is a work in progress, Latest version is merged to main branch but older versions are accessible in appropriately named branches.

# Installation
1. pip install PyPDF2
2. pip install tf-keras
3. pip install groq
4. pip install adalflow
5. pip install transformers


# Run application
Run the application using the below command

```uvicorn main:app --reload```

1. Hit this API to extract pdf content

``` curl -X POST http://127.0.0.1:8000/chunk/doc ```

2. Access any of the GET endpoints (ex:http://127.0.0.1:8000/chat/adal?query=%27sample%27) to generate response