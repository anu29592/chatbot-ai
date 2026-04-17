
import os
from dotenv import load_dotenv
from typing import Callable
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from document_loader import load_all_documents
from langchain_core.messages import HumanMessage
load_dotenv()
print(os.getenv("GOOGLE_API_KEY"))

def create_rag_chain() -> Callable[[str], str]:
    # 1. Load and split documents
    # Ensure load_all_documents() returns a list of strings or Documents
    raw_docs = load_all_documents() 
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    
    # If raw_docs is a list of strings:
    doc_objs = splitter.create_documents(raw_docs)
    # If raw_docs is already a list of Document objects, use:
    # doc_objs = splitter.split_documents(raw_docs)

    if not doc_objs:
        raise ValueError("No documents loaded for RAG pipeline.")

    # 2. Embeddings (local)
    # This won't trigger the 'unhashable' error because it's the official class
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 3. Vector store
    vectorstore = FAISS.from_documents(doc_objs, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    
    # 4. LLM (Gemini)
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0.2,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    def qa_chain(query: str) -> str:
        if not query.strip():
            return "Please enter a valid question."
        
        # Retrieval
        retrieved_docs = retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])
        
        # Prompting
        prompt = (
            f"Use the following pieces of retrieved context to answer the question. "
            f"If you don't know the answer, just say that you don't know.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {query}\n"
            f"Answer:"
        )
        
        try:
            response = llm.invoke([HumanMessage(content=prompt)])
            return response.content
        except Exception as e:
            return f"Error invoking LLM: {str(e)}"

    return qa_chain