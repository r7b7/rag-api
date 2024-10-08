from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "RAG API"
    
    # Model Settings
    EMBEDDING_MODEL: str = "intfloat/e5-small"
    GENERATOR_MODEL: str = "gemma2-9b-it"
    SUMMARIZER_MODEL: str = "facebook/bart-large-cnn"
    
    # Vector Store Settings
    VECTOR_STORE_TYPE: str = "chroma"
    VECTOR_STORE_PATH: str = "data/vectorstore"

    # Text Splitter Settings
    SPLIT_BY: str = "sentence"
    CHUNK_SIZE: int = 5
    CHUNK_OVERLAP: int = 2

    class Config:
        env_file = ".env"

settings = Settings()