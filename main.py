from rag.adal_pipeline import ChatGenerator
from rag.doc_massager import extract_pdf_content, fetch_similar_record
from rag.response_generator_gpt2 import generate_response_from_llm
from rag.response_generator_gpt4 import generate_response
from rag.summarizer import summarize_retrieved_doc

from typing import Optional
from fastapi import FastAPI
from adalflow.components.model_client import GroqAPIClient
import time


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Health Check! 200 OK!"}

@app.get("/chat/gpt2")
def get_chat_response_gpt2(query: Optional[str] = "A fact on olympics"):
    retrieved_doc = fetch_similar_record(query)    
    summarized_doc = summarize_retrieved_doc(retrieved_doc)
    start_time = time.time()
    response = generate_response_from_llm(query + " "+ summarized_doc)
    end_time = time.time()
    print(f"Elapsed time Gpt2: {end_time - start_time} seconds")
    return response

@app.get("/chat")
def get_chat_response_gpt4(query: Optional[str] = "A fact on olympics"):
    retrieved_doc = fetch_similar_record(query)    
    summarized_doc = summarize_retrieved_doc(retrieved_doc)
    start_time = time.time()
    response = generate_response(query + " "+ summarized_doc)
    end_time = time.time()
    print(f"Elapsed time Gpt4: {end_time - start_time} seconds")
    return response

@app.get("/chat/adal")
def get_chat_response_adal(query: Optional[str] = "A fact on olympics"):
    generator = ChatGenerator(
        model_client=GroqAPIClient(),
        model_kwargs={"model": "gemma2-9b-it"},
    )
    retrieved_doc = fetch_similar_record(query)   
    summarized_doc = summarize_retrieved_doc(retrieved_doc)
    start_time = time.time()
    response = generator(query + " "+ summarized_doc)
    end_time = time.time()
    print(f"Elapsed time Adal: {end_time - start_time} seconds")
    return response

@app.post("/chunk/doc")
def store_doc_chunks():
    extract_pdf_content()
    return "success"

if __name__ == "__main__":
   pass