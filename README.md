# RAG - API

This is a work in progress, lot of hardcoded stuff to remove.

#Installation
1.pip install PyPDF2
2.pip install tf-keras
3.pip install groq
4.pip install adalflow
5.pip install transformers

#Run application
Run the application using the below command

```uvicorn main:app --reload```

Access the endpoint at http://127.0.0.1:8000/chat/adal?query=%27sample%27 