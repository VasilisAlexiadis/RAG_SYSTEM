from rag.pipeline import LangChainRAG

def test_query():
    rag = LangChainRAG()
    result = rag.query("What is the topic of these documents?")
    assert "answer" in result
