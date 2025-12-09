# 🇮🇳 **BharatGPT – AI Chatbot for Everything About India**

### *An AI-powered knowledge assistant built using Streamlit, FAISS Vector Store, and OpenAI.*

BharatGPT is an intelligent RAG-based chatbot that answers any question related to **India’s history, geography, culture, constitution, tourism, festivals, and more**.
It uses **PDF/Text embedding + semantic search + LLM** to provide accurate, context-aware responses.

---

## 🚀 **Features**

* 📄 Upload and process large PDF/Text datasets
* 🔍 Semantic search powered by **FAISS vector store**
* 🤖 Intelligent answers using **OpenAI Chat Models**
* 🇮🇳 India-specific curated dataset
* ⚡ Fast and lightweight Streamlit UI
* 📚 Easy to extend — add more `.txt` files anytime
* 🔐 Secure — API key stored locally
* 🧠 Works like a mini-GPT built only for India

---

## 🏗️ **Tech Stack**

| Component       | Tech Used                      |
| --------------- | ------------------------------ |
| Frontend        | Streamlit                      |
| Backend         | Python                         |
| Embeddings      | OpenAI Embeddings              |
| Vector DB       | FAISS                          |
| LLM             | ChatOpenAI                     |
| Text Splitting  | RecursiveCharacterTextSplitter |
| Version Control | Git & GitHub                   |

---

## 📂 **Project Structure**

```
bharatgpt/
│
├── app.py                # Streamlit UI + chatbot logic
├── ingest.py             # Creates vector embeddings & FAISS store
│
├── data/                 # Raw text files (Indian information)
│   ├── history.txt
│   ├── geography.txt
│   ├── culture.txt
│   ├── constitution.txt
│   ├── tourism.txt
│   ├── facts.txt
│   └── festivals.txt     # (or additional categories)
│
├── vector_store/         # Generated FAISS vector DB
│   ├── index.faiss
│   ├── index.pkl
│
├── requirements.txt
└── README.md
```

---

## ⚙️ **How to Run BharatGPT**

### **1. Clone the repository**

```
git clone https://github.com/your-username/bharatgpt.git
cd bharatgpt
```

### **2. Create Virtual Environment**

```
python -m venv .venv
```

### **3. Activate Virtual Environment**

```
.venv\Scripts\activate
```

### **4. Install Dependencies**

```
pip install -r requirements.txt
```

### **5. Add your API Key**

Create a `.env` file:

```
OPENAI_API_KEY="your_api_key_here"
```

(Or put directly inside app.py — not recommended)

---

## 🔍 **6. Create Vector Store**

Run:

```
python ingest.py
```

This reads all `.txt` files from `/data` and creates FAISS embeddings.

---

## 💬 **7. Start BharatGPT**

```
streamlit run app.py
```

Your chatbot is now live!
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 📌 **Example Questions You Can Ask**

* “Tell me about the Mughal Empire”
* “What are the major rivers of India?”
* “Important articles of the Indian Constitution?”
* “Famous festivals in Maharashtra”
* “Top tourist places in Rajasthan”
* “List of classical dance forms of India”

---

## 🛠️ **Future Enhancements**

* 🎤 Voice-based question input
* 🌍 Add multilingual support (Hindi, Marathi, Tamil, etc.)
* 🧭 Better UI using custom CSS
* 📚 Add more categories like:

  * Indian economy
  * Freedom fighters
  * Government schemes
  * Awards & sports
  * States & union territories

---

## ❤️ **Creator**

Built with love by **Tanishka (Sakhi)**
Passionate about AI, ML, Cloud & Full Stack Development.

---

## ⭐ **Show Support**

If you like this project:

✔ Star ⭐ the repository
✔ Share it on LinkedIn
✔ Contribute more datasets


