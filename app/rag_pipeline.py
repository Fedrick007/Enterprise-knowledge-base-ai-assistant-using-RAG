from langchain_openai import ChatOpenAI
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from app.document_loader import load_documents
from app.vector_store import create_vector_store

class RAGPipeline:
    def __init__(self):
        # 1. Load and Vectorize
        documents = load_documents()
        if not documents:
            print("Warning: Knowledge base is empty. AI will answer from general knowledge.")
        self.vectorstore = create_vector_store(documents)
        
        # 2. Setup the LLM
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0
        )
        
        # 3. Initialize the modernized chain
        self.qa_chain = self._create_qa_chain()

    def _create_qa_chain(self):
        # Define a specific system prompt for your Enterprise Knowledge Base
        system_prompt = (
            "Use the following pieces of retrieved context to answer the user's question. "
            "If you don't know the answer, just say that you don't know. "
            "Keep the answer concise.\n\n"
            "{context}"
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])

        # Create the chain that handles document formatting
        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)
        
        # Create the final retrieval chain
        return create_retrieval_chain(
            self.vectorstore.as_retriever(), 
            question_answer_chain
        )

    def ask(self, question: str):
        # Use .invoke() instead of calling the object directly
        response = self.qa_chain.invoke({"input": question})

        # In create_retrieval_chain, the keys are "answer" and "context"
        sources = [
            doc.metadata.get("source", "Unknown")   #list comprehension
            for doc in response["context"]
        ]

        return {
            "answer": response["answer"],
            "sources": list(set(sources)) # Set removes duplicates
        }
