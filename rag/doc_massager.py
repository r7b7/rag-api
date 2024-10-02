import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text_array = []
vectorizer = TfidfVectorizer()

def extract_pdf_content():
    with open("files/olympics.pdf", "rb") as file: #file read as binary data
        reader = PyPDF2.PdfReader(file)  
        num_pages = len(reader.pages)  
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text_array.append(page.extract_text())

def vectorize_extracted_content():
    tfidf_matrix = vectorizer.fit_transform(text_array)
    return tfidf_matrix

def fetch_similar_record(query):
    tfidf_matrix = vectorize_extracted_content()
    query_vector = vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)

    top_doc_index = similarity_scores.argmax()
    retrieved_doc = text_array[top_doc_index]
    return retrieved_doc



   
