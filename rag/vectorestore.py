from langchain_community.vectorstores import Chroma
from rag.embeddings import get_embeddings
from app.settings import settings

def get_vectorstore():
    embeddings = get_embeddings()

    return Chroma(
        collection_name="documents",
        embedding_function=embeddings,
        persist_directory=settings.CHROMA_PATH
    )
