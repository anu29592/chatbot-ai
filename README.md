# 🤖 AI Chatbot with RAG (Gemini + HuggingFace + LangChain + FAISS)

A simple AI chatbot that answers questions from multi-format documents and fetches dynamic data from external services.

---

##  Features

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
git clone https://github.com/anu29592/chatbot-ai.git

```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux

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

How do we request a vacation?
what are coding standards for formatting?
what are benefits of company policy?



### 🌐 Dynamic (External API)

* "How many vacation days do I have left?"

---


## 🧪 Tech Stack

* Python
* Streamlit
* LangChain
* Google Gemini (LLM) & HuggingFace (Local Embeddings)
* FAISS
* PyPDF2

---



## 👨‍💻 Author

Archana Aswathaiah

---



