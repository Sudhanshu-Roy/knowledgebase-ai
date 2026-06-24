# 📚 KnowledgeBase AI

### Chat with Your Documents. Instantly.

KnowledgeBase AI is a Retrieval-Augmented Generation (RAG) powered SaaS application that transforms static documents into an intelligent conversational knowledge base.

Upload PDFs such as company policies, employee handbooks, research papers, product documentation, onboarding guides, or internal knowledge repositories and ask questions in natural language. The application retrieves the most relevant information from the uploaded documents and generates context-aware responses using Groq-powered LLMs.

---

## 🌐 Live Demo

**Live Application:** https://knowledgebase-ai-chatbot.streamlit.app/

---

## 🎯 Problem Statement

Organizations generate massive amounts of knowledge in the form of PDFs, documentation, policies, reports, onboarding guides, research papers, and internal manuals.

The challenge is not storing information — it's finding the right information at the right time.

Traditional document search methods require users to manually browse hundreds of pages to locate specific answers, resulting in:

* Time-consuming information retrieval
* Reduced productivity
* Knowledge silos
* Repetitive questions
* Poor onboarding experiences

KnowledgeBase AI solves this problem by transforming documents into a searchable AI-powered knowledge assistant that can understand context, retrieve relevant information, and answer questions conversationally.

---

## 💡 Solution Overview

KnowledgeBase AI combines Retrieval-Augmented Generation (RAG), semantic search, vector databases, and Large Language Models to create an intelligent document assistant.

Instead of relying on model memory, the system:

1. Extracts content from uploaded documents
2. Splits content into meaningful chunks
3. Generates vector embeddings
4. Stores embeddings inside ChromaDB
5. Retrieves relevant context for each query
6. Uses Groq LLMs to generate grounded responses
7. Displays source citations for transparency

This ensures responses remain accurate, relevant, and traceable to the original documents.

---

## ✨ Features

### 📄 Document Upload

* Upload PDF documents
* Automatic content extraction
* Multi-page document support

### 🧠 Retrieval-Augmented Generation (RAG)

* Intelligent semantic search
* Context-aware responses
* Reduced hallucinations
* Document-grounded answers

### ⚡ Fast AI Responses

* Powered by Groq LLMs
* Low-latency inference
* Real-time interaction

### 🔍 Source Citations

* Display source documents
* Show referenced pages
* Improve answer transparency

### 💬 Conversational Interface

* ChatGPT-style interaction
* Natural language queries
* Follow-up questioning support

### ☁️ Cloud Deployment

* Publicly accessible Streamlit application
* Mobile-friendly interface
* Cross-platform support

---

## 🏗️ System Architecture

```text
                    ┌──────────────┐
                    │ PDF Uploads  │
                    └──────┬───────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Document Loader    │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Text Chunking      │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Embeddings Model   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Chroma Vector DB   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Retriever          │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Groq LLM           │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ AI Response        │
                └────────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### AI & LLM

* Groq
* LangChain

### Embeddings

* HuggingFace Embeddings
* all-MiniLM-L6-v2

### Vector Database

* ChromaDB

### Document Processing

* PyPDFLoader
* RecursiveCharacterTextSplitter

### Backend Logic

* Python

### Deployment

* Streamlit Community Cloud

---

## 📸 Screenshots

### Home Interface

<img width="956" height="467" alt="Screenshot 2026-06-24 120914" src="https://github.com/user-attachments/assets/82887887-c305-4403-9f89-6f14937a3b87" />

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/Sudhanshu-Roy/knowledgebase-ai.git

cd knowledgebase-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## 📊 Skills Demonstrated

This project demonstrates practical experience with:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embedding Models
* Semantic Search
* LangChain
* Groq LLM Integration
* Document Processing Pipelines
* Streamlit Deployment
* Prompt Engineering
* End-to-End AI Product Development

---

## 🔮 Future Improvements

* Multi-document collections
* User authentication
* Multiple knowledge bases
* DOCX support
* Conversation memory
* Admin dashboard
* Team collaboration
* Citation highlighting
* Knowledge base analytics

---

## 👨‍💻 Author

Built by Sudhanshu Roy as part of an AI Engineering portfolio focused on Retrieval-Augmented Generation (RAG), LLM Applications, and Full-Stack AI Development.

---

## ⭐ If you found this project interesting

Consider giving the repository a star and connecting with me on LinkedIn.
