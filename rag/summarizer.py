from transformers import pipeline

#specify model
def summarize_retrieved_doc(retrieved_doc):
    summarizer = pipeline("summarization")
    summary = summarizer(retrieved_doc, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    return summary


