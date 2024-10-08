from app.config import settings
from adalflow.components.data_process.text_splitter import TextSplitter


class SentenceSplitter:
    def __init__(self, split_by=settings.SPLIT_BY):
        self.split_by = split_by
        self.chunk_size = settings.CHUNK_SIZE
        self.chunk_overlap = settings.CHUNK_OVERLAP

    def split_text_to_chunks(self, text_to_split):
        text_splitter = TextSplitter(self.split_by, self.chunk_size,self.chunk_overlap)
        text_chunks = text_splitter.split_text(text_to_split)
        return text_chunks
