import PyPDF2
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel

text_array = []
model_name = "intfloat/e5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def extract_pdf_content():
    with open("files/olympics.pdf", "rb") as file: #file read as binary data
        reader = PyPDF2.PdfReader(file)  
        num_pages = len(reader.pages)  
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text_array.append(page.extract_text())

def get_doc_embedding(para):
    inputs = tokenizer(para, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1)  
    return embedding.squeeze().numpy()


def fetch_similar_record(query):
    doc_embeddings = np.array([get_doc_embedding(para) for para in text_array])
    query_embedding = get_doc_embedding(query)
    query_embedding = query_embedding.reshape(1, -1)
    similarities = cosine_similarity(query_embedding, doc_embeddings)
    most_similar_index = np.argmax(similarities)
    retrieved_doc = text_array[most_similar_index]
    return retrieved_doc

   
