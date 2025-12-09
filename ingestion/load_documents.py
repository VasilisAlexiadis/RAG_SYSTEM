from ingestion.parse import parse_pdf
from rag.chunking import chunk_text
import os

try:
    # Preferred import when langchain is available
    from langchain.schema import Document
except Exception:
    # Minimal fallback Document class to avoid hard dependency in tests
    class Document:
        def __init__(self, page_content: str, metadata: dict | None = None):
            self.page_content = page_content
            self.metadata = metadata or {}


def load_documents(folder="data/raw"):
    docs = []

    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            raw_text = parse_pdf(os.path.join(folder, file))
            chunks = chunk_text(raw_text)

            for idx, chunk in enumerate(chunks):
                docs.append(
                    Document(
                        page_content=chunk,
                        metadata={"file": file, "chunk": idx}
                    )
                )

    return docs
