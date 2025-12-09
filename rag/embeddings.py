from langchain_community.embeddings import HuggingFaceEmbeddings
from app.settings import settings

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL,
        encode_kwargs={"normalize_embeddings": True}
    )
