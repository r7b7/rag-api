from app.config import settings
from transformers import pipeline


class Summarizer:
    def __init__(self, model_name=settings.SUMMARIZER_MODEL):
        self.model_name = model_name
        
    
    def summarize(self, doc_to_summarize):
        summarizer = pipeline("summarization", model=self.model_name)
        summary = summarizer(doc_to_summarize, max_length=400, min_length=30, do_sample=False)[0]['summary_text']
        return summary