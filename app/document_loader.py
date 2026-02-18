import os
from langchain_community.document_loaders import PyPDFLoader

def load_documents(data_path="data"):
    documents = []

    if not os.path.exists(data_path):
        raise ValueError("Data folder not found.")

    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(data_path, file)
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())

    if not documents:
        raise ValueError("No PDF documents found in data folder.")

    return documents
