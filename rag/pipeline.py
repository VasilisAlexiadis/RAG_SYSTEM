from rag.vectorestore import get_vectorstore
from rag.llm import get_llm
from rag.prompts import rag_prompt

try:
    from langchain.chains import RetrievalQA
except Exception:
    RetrievalQA = None

class LangChainRAG:
    def __init__(self):
        self.llm = get_llm()
        self.vstore = get_vectorstore()
        try:
            self.retriever = self.vstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 5}
            )

            # RetrievalQA chain (LangChain)
            if RetrievalQA is None:
                raise RuntimeError("LangChain not available")

            self.chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                retriever=self.retriever,
                chain_type="stuff",
                return_source_documents=True
            )
        except Exception:
            # Fallback simple chain when dependencies or services aren't available
            class _FallbackChain:
                def __call__(self, payload: dict):
                    return {"result": "[fallback] no LLM available", "source_documents": []}

            self.chain = _FallbackChain()

    def query(self, question: str):
        result = self.chain({"query": question})

        answer = result["result"]
        sources = [
            {
                "metadata": doc.metadata,
                "preview": doc.page_content[:250]
            }
            for doc in result["source_documents"]
        ]

        return {
            "answer": answer,
            "sources": sources
        }
