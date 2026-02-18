# 📚 Enterprise RAG AI Assistant

A production-ready **Retrieval-Augmented Generation (RAG) AI Assistant** built using Large Language Models (LLMs), LangChain, FAISS, and FastAPI.

This system allows users to upload PDF documents and ask context-aware questions. It retrieves relevant information using vector search and generates accurate responses using OpenAI models.

---

## 🚀 Features

- End-to-End Retrieval-Augmented Generation (RAG) Pipeline  
- PDF Document Ingestion  
- Intelligent Text Chunking Strategy  
- OpenAI Embeddings Generation  
- FAISS Vector Database for Semantic Search  
- Context-Aware Question Answering  
- REST API using FastAPI  
- Modular and Scalable Architecture  
- Docker-Ready Deployment  
- Source Citation Support  
- Hallucination Reduction via Retrieval Grounding  

---

## 🏗️ System Architecture

1. Load PDF documents from `data/` folder  
2. Split documents into chunks  
3. Generate embeddings using OpenAI  
4. Store embeddings in FAISS vector database  
5. Accept user question via API  
6. Retrieve relevant chunks using semantic search  
7. Pass retrieved context to LLM  
8. Generate final grounded response  

---

## 📂 Project Structure

```
Enterprise-knowledge-base-ai-assistant-using-RAG/
│
├── app/
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── document_loader.py
│   ├── vector_store.py
│   ├── schemas.py
│   └── config.py
│
├── data/
│   └── (Add PDF files here)
│
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

## 🛠️ Tech Stack

- Python  
- FastAPI  
- LangChain  
- OpenAI API  
- FAISS (Vector Database)  
- Pydantic  
- Uvicorn  
- Docker  

---

## 🔧 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Enterprise-knowledge-base-ai-assistant-using-RAG.git
cd Enterprise-knowledge-base-ai-assistant-using-RAG
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

### 5️⃣ Add PDF Documents

Place your PDF files inside the `data/` folder.

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

Use the `/ask` endpoint to submit questions.

---

## 🐳 Docker Setup

### Build Docker Image

```bash
docker build -t rag-ai .
```

### Run Container

```bash
docker run -p 8000:8000 rag-ai
```

---

## 📌 Example API Request

**POST** `/ask`

```json
{
  "question": "What are the key responsibilities mentioned in the document?"
}
```

### Example Response

```json
{
  "answer": "The key responsibilities include...",
  "sources": ["data/sample.pdf"]
}
```

---

## 📈 Engineering Highlights

- Designed modular RAG architecture  
- Implemented document chunking & embeddings  
- Built FAISS-based vector search system  
- Integrated OpenAI LLM with retrieval pipeline  
- Developed FastAPI-based AI microservice  
- Containerized application using Docker  
- Structured scalable backend design  

---

## 🎯 Resume Value

This project demonstrates:

- Large Language Models (LLMs)  
- Generative AI System Design  
- Retrieval-Augmented Generation (RAG)  
- Vector Databases & Embeddings  
- Backend API Development  
- Dockerized Deployment  
- Scalable AI Microservice Architecture  

---

## 🔮 Future Enhancements

- Persistent FAISS storage  
- Chat memory support  
- Multi-user authentication  
- Cloud deployment (AWS/GCP/Azure)  
- Hallucination evaluation framework  
- Open-source LLM integration  

---

## 👨‍💻 Author

Fedrick Samuel W - 
Software Engineer | Python Developer  

