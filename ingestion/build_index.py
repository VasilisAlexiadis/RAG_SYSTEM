from ingestion.load_documents import load_documents
from rag.vectorestore import get_vectorstore

def build_index():
    docs = load_documents()
    vstore = get_vectorstore()

    texts = [d.page_content for d in docs]
    metas = [d.metadata for d in docs]

    vstore.add_texts(texts, metadatas=metas)
    vstore.persist()

    print("Index created successfully.")

if __name__ == "__main__":
    build_index()
