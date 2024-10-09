from transformers import AutoTokenizer, AutoModel
from app.config import settings
import torch

class TransformerEmbedder():
    def __init__(self, model_name=settings.EMBEDDING_MODEL):
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.load_model()

    def load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModel.from_pretrained(self.model_name)
        
    def get_embeddings(self, text_to_embed):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        inputs = self.tokenizer(text_to_embed, return_tensors='pt', padding=True).to(device)
        self.model.to(device)
        with torch.no_grad():
            outputs = self.model(**inputs)
        embedding = outputs.last_hidden_state.mean(dim=1)  
        return embedding.squeeze().numpy()