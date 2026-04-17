

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import google.generativeai as genai
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from document_loader import load_all_documents
from typing import Callable, Any

load_dotenv()
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

def list_available_models() -> None:
    """Print available Google Generative AI models."""
    print("Available Google Generative AI models:")
    for model in genai.list_models():
        print(model.name)

list_available_models()


def create_rag_chain() -> Callable[[str], Any]:
    """
    Create a Retrieval-Augmented Generation (RAG) QA chain.
    Returns a function that takes a query string and returns an answer from the LLM.
    """
    # 1. Load and split documents
    raw_docs = load_all_documents()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = [chunk for text in raw_docs for chunk in splitter.create_documents([text])]

    # 2. Embeddings (Gemini)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2-preview")
    texts = [doc.page_content for doc in docs]

    # 3. Vector DB (FAISS)
    from langchain_core.documents import Document
    doc_objs = [Document(page_content=text) for text in texts]
    class DummyEmbeddings:
        def embed_documents(self, texts):
            return [embeddings.embed_documents([text])[0] for text in texts]
        def embed_query(self, text):
            return embeddings.embed_documents([text])[0]
        def __call__(self, text):
            return self.embed_query(text)
    vectorstore = FAISS.from_documents(doc_objs, DummyEmbeddings())
    retriever = vectorstore.as_retriever()

    # 4. LLM (Gemini)
    llm = ChatGoogleGenerativeAI(model="models/gemini-3.1-flash-lite-preview")

    def qa_chain(query: str) -> str:
        """
        Retrieve relevant docs and generate an answer using the LLM.
        """
        docs = retriever.invoke(query)
        context = "\n".join([doc.page_content for doc in docs])
        prompt = f"Answer the question based on the following context:\n{context}\n\nQuestion: {query}\nAnswer:"
        try:
            response = llm.invoke(prompt)
        except Exception as e:
            print(f"Error invoking LLM: {e}")
            return "Sorry, there was an error generating a response."

        # Handle response as dict with 'content' key
        if isinstance(response, dict) and "content" in response:
            content = response["content"]
            print(f"LLM response content: {content}")
            print(f"LLM response content type: {type(content)}")
            print(f"LLM response content sample: {response}")
            # If content is a list of dicts with 'text' key
            if isinstance(content, list) and isinstance(content[0], dict) and "text" in content[0]:
                return content[0]["text"]
            # If content is a string, return it directly
            if isinstance(content, str):
                return content
            # If content is a list of strings
            if isinstance(content, list) and isinstance(content[0], str):
                return content[0]
            # Fallback: return string representation
            return str(content)
        if isinstance(response, str):
            
            return response["content"][0]["text"]
        # If response is a list of dicts with 'text' key
        if isinstance(response, list) and isinstance(response[0], dict) and "text" in response[0]:
            return response["content"][0]["text"]
        # If response is a list of strings
        if isinstance(response, list) and isinstance(response, str):
            return response["content"][0]["text"]
        # Fallback: return string representation
        print(f"LLM response type: {type(response)}")
        print(f"LLM response content: {response}")
        return str(response.content[0]["text"])

    return qa_chain