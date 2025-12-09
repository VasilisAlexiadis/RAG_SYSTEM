from fastapi import APIRouter
from pydantic import BaseModel
from rag.pipeline import LangChainRAG

router = APIRouter()
rag = LangChainRAG()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
def query_rag(req: QueryRequest):
    return rag.query(req.question)
