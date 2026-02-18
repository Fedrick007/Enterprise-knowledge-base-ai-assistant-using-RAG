from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from app.document_loader import load_documents
from app.vector_store import create_vector_store


class RAGPipeline:

    def __init__(self):
        documents = load_documents()
        self.vectorstore = create_vector_store(documents)
        self.qa_chain = self._create_qa_chain()

    def _create_qa_chain(self):
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=self.vectorstore.as_retriever(),
            return_source_documents=True
        )

        return qa_chain

    def ask(self, question: str):
        response = self.qa_chain(question)

        sources = [
            doc.metadata.get("source", "Unknown")
            for doc in response["source_documents"]
        ]

        return {
            "answer": response["result"],
            "sources": sources
        }
