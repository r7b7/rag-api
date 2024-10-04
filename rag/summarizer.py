from transformers import pipeline

def summarize_retrieved_doc(retrieved_doc):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(retrieved_doc, max_length=400, min_length=30, do_sample=False)[0]['summary_text']
    return summary


