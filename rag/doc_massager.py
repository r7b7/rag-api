import PyPDF2
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
import chromadb

client = chromadb.Client()
collection = client.create_collection("olympics_wiki_collection")


def extract_pdf_content():
    text_array = []
    with open("files/olympics.pdf", "rb") as file: #file read as binary data
        reader = PyPDF2.PdfReader(file)  
        num_pages = len(reader.pages)  
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text_array.append(page.extract_text())

    store_embedding(text_array)

def get_doc_embedding(para):
    model_name = "intfloat/e5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    
    inputs = tokenizer(para, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1)  
    return embedding.squeeze().numpy()

def store_embedding(text_array):
    collection.add(
        embeddings= [get_doc_embedding(para).tolist() for para in text_array],
        documents=[para for para in text_array],
        ids=[f"{i}" for i in range(len(text_array)) ]
    )


def fetch_similar_record(query):
    query_embedding = get_doc_embedding(query)
    retrieved_embedding= collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=1,
        include=["documents"]
    )
    retrieved_doc = retrieved_embedding['documents'][0][0]
    return retrieved_doc


