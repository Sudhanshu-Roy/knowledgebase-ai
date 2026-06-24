import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import tempfile
from langchain_text_splitters import (RecursiveCharacterTextSplitter)
from langchain_huggingface import (HuggingFaceEmbeddings)
from langchain_community.vectorstores import (Chroma)
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

if "messages" not in st.session_state:
    st.session_state.messages = []

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

st.set_page_config(
    page_title="KnowledgeBase AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 KnowledgeBase AI")

st.caption(
    "Upload company documents and chat with your knowledge base."
)

with st.sidebar:

    st.header("Documents")
    uploaded_file = st.file_uploader("Upload PDF",type=["pdf"])

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(
            uploaded_file.getvalue()
        )

        pdf_path = temp_file.name

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    chunks = splitter.split_documents(docs)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="./chroma_db"
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    question = st.chat_input("Ask a question...")

    if question:
        context = "\n\n".join(doc.page_content for doc in docs)
        prompt = f"""
You are a company knowledge assistant.
Answer ONLY from the provided context.
If the answer is not contained in the context, say:
"I could not find that information in the uploaded documents."

Context: {context}
Question: {question}
"""

        response = llm.invoke(prompt)

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response.content
            }
        )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
