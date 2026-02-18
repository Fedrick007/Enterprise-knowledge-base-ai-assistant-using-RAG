import os
from langchain_community.document_loaders import PyPDFLoader

def load_documents(data_path="data"):
    documents = []
    
    # Ensure path is absolute to avoid MINGW64 pathing issues
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_data_path = os.path.join(base_dir, data_path)

    if not os.path.exists(full_data_path):
        # Create the folder if it doesn't exist instead of crashing
        os.makedirs(full_data_path)
        print(f"Created missing directory: {full_data_path}")
        return []

    for file in os.listdir(full_data_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(full_data_path, file)
            loader = PyPDFLoader(file_path)
            # Use extend for better structure
            documents.extend(loader.load())

    return documents
