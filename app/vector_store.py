from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


def create_vector_store(documents):
    # 1. Check if documents actually exist
    if not documents:
        print("Warning: No documents provided. Creating an empty vector store is not supported by FAISS.")
        return None

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    
    # 2. Check if splitting resulted in any text chunks
    if not texts:
        print("Warning: Documents were found but no text could be extracted.")
        return None

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(texts, embeddings)
    return vectorstore

