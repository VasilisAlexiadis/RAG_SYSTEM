try:
    from pydantic import BaseSettings

    class Settings(BaseSettings):
        CHROMA_PATH: str = "chroma/"
        EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
        OLLAMA_MODEL: str = "llama3.2"

    settings = Settings()
except Exception:
    # Minimal fallback when pydantic isn't available or has incompatible version
    from dataclasses import dataclass

    @dataclass
    class Settings:
        CHROMA_PATH: str = "chroma/"
        EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
        OLLAMA_MODEL: str = "llama3.2"

    settings = Settings()
