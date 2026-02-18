from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from app.schemas import QueryRequest, QueryResponse
from app.rag_pipeline import RAGPipeline

# Global variable for the pipeline
rag_pipeline = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the RAG model on startup
    global rag_pipeline
    try:
        print("Initializing RAG Pipeline (Loading documents...)...")
        rag_pipeline = RAGPipeline()
        print("RAG Pipeline Ready!")
        yield
    finally:
        # Clean up resources if needed
        print("Shutting down...")

app = FastAPI(
    title="Enterprise RAG AI Assistant",
    lifespan=lifespan
)

@app.get("/")
def health_check():
    return {"status": "RAG AI Assistant Running"}

@app.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    if not rag_pipeline:
        raise HTTPException(status_code=503, detail="RAG Pipeline not initialized")
    
    try:
        # Using a threadpool for the heavy AI logic
        result = rag_pipeline.ask(request.question)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
