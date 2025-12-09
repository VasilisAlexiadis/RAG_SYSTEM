from langchain_ollama import OllamaLLM
from app.settings import settings

def get_llm():
    return OllamaLLM(
        model=settings.OLLAMA_MODEL,
        # optional but recommended for stability
        base_url="http://localhost:11434",
        temperature=0.1,
    )
