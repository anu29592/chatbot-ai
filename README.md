# 🤖 AI Chatbot with RAG (Gemini + LangChain + FAISS)

A simple AI chatbot that answers questions from multi-format documents and fetches dynamic data from external services.

---

## 🚀 Features

* 📄 Multi-format document support (PDF, Markdown, TXT)
* 🧠 Retrieval-Augmented Generation (RAG)
* ⚡ Fast similarity search with FAISS
* 🤖 Google Gemini (LLM) & HuggingFace (Local Embeddings)
* 🌐 Dynamic data via external API (mocked)
* 🎨 Simple UI using Streamlit

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-chatbot-rag.git
cd ai-chatbot-rag
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

```bash
cp .env.example .env
```

Add your Google API key:

```
GOOGLE_API_KEY=your_key_here
```

---

### 5. Run the app

```bash
streamlit run app/main.py
```

---

## 💬 Example Queries

### 📚 Static (RAG)

* "What is the company vacation policy?"
* "Explain onboarding guidelines"

### 🌐 Dynamic (External API)

* "How many vacation days do I have left?"

---

## 🧠 Design Decisions

### 1. RAG over fine-tuning

* Lightweight and scalable
* No need for model retraining

### 2. FAISS for vector search

* Fast and efficient similarity retrieval
* Works locally without external services

### 3. Rule-based routing

* Simple and transparent
* Easy to extend

---

## 🔄 Future Improvements

* Replace rule-based routing with LLM-based intent classification
* Add chat memory (conversation history)
* Persist FAISS index
* Integrate real backend APIs
* Add authentication
* Deploy on AWS (S3, Lambda, API Gateway)

---

## 🧪 Tech Stack

* Python
* Streamlit
* LangChain
* Google Gemini (LLM) & HuggingFace (Local Embeddings)
* FAISS
* PyPDF2

---

## 📸 Screenshot

*Add a screenshot here (screenshots/ui.png)*

---

## 👨‍💻 Author

Your Name

---

## ⭐ Notes

This project is intentionally simple and focuses on:

* Clean architecture
* Separation of concerns
* Demonstrating RAG + external integrations

---
