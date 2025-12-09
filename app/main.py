from fastapi import FastAPI
from app.routes.query import router as query_router
from app.routes.health import router as health_router

app = FastAPI(title="Enterprise RAG (LangChain + Ollama)")

app.include_router(query_router, prefix="/api")
app.include_router(health_router, prefix="/api")
