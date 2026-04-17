import streamlit as st
from dotenv import load_dotenv

from rag_pipeline import create_rag_chain
from external_service import get_vacation_days

load_dotenv()

st.set_page_config(page_title="AI Chatbot", layout="wide")

st.title("Company ChatBot")

# Initialize RAG
if "qa_chain" not in st.session_state:
    with st.spinner("Loading documents..."):
        st.session_state.qa_chain = create_rag_chain()


# Chat UI
query = st.text_input("Ask a question:")

def maybe_fetch_external(query):
    # Let the LLM decide, but as a simple example, check for keywords
    vacation_keywords = ["vacation days", "days left", "vacation balance", "leave balance"]
    if any(k in query.lower() for k in vacation_keywords):
        data = get_vacation_days("user123")
        return f"You have {data['remaining_days']} vacation days left."
    return None

if query:
    # Try external fetch first
    ext_response = maybe_fetch_external(query)
    if ext_response:
        response = ext_response
    else:
        response = st.session_state.qa_chain(query)
    st.write(" Answer:")
    if isinstance(response, dict) and "content" in response:
        st.write(response["content"])
    else:
        st.write(response)