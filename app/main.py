from fastapi import FastAPI
from app.schemas import QueryRequest, QueryResponse
from app.rag_pipeline import RAGPipeline

app = FastAPI(title="Enterprise RAG AI Assistant")

rag = RAGPipeline()


@app.get("/")
def health_check():
    return {"status": "RAG AI Assistant Running"}


@app.post("/ask", response_model=QueryResponse)
def ask_question(request: QueryRequest):
    result = rag.ask(request.question)
    return result
