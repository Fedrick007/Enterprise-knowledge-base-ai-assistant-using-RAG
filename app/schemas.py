from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    # Specifying list[str] makes your API docs much cleaner
    sources: list[str] 
