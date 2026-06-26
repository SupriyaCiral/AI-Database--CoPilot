# 🤖 FastAPI Ollama Chatbot

An AI chatbot backend built using **FastAPI** and **Ollama**, capable of running Large Language Models (LLMs) locally without relying on cloud APIs.

---

## 🚀 Features

- FastAPI REST API
- Local AI inference using Ollama
- Supports **Llama 3** and **Qwen** models
- Request & Response validation using Pydantic
- Modular project architecture
- Logging support
- Interactive Swagger API documentation

---

## 🛠️ Tech Stack

- Python 3.13
- FastAPI
- Uvicorn
- Ollama
- Llama 3
- Qwen2.5-Coder
- HTTPX
- Pydantic
- Git & GitHub

---

## 📁 Project Structure

```text
FastAPI-Ollama-Chatbot
│
├── app
│   ├── core
│   │     └── logger.py
│   │
│   ├── models
│   │     └── schemas.py
│   │
│   ├── services
│   │     └── ollama_service.py
│   │
│   ├── config.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/SupriyaCiral/fastapi-ollama-chatbot.git
```

Navigate to the project

```bash
cd fastapi-ollama-chatbot
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python -m uvicorn app.main:app --reload
```

Server runs at

```
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## 📤 Example Request

```json
{
    "question": "Explain Retrieval-Augmented Generation (RAG)"
}
```

---

## 📥 Example Response

```json
{
    "question": "Explain Retrieval-Augmented Generation (RAG)",
    "answer": "Retrieval-Augmented Generation (RAG) combines information retrieval with large language models..."
}
```

---

## 🏗️ Architecture

```text
                User
                  │
                  ▼
          FastAPI REST API
                  │
                  ▼
          Ollama Service Layer
                  │
                  ▼
        Local LLM (Llama 3 / Qwen)
                  │
                  ▼
             AI Response
```

---

## 🔮 Future Improvements

- Conversation history
- Chat memory
- Streaming responses
- React frontend
- Docker support
- Authentication
- Multi-model switching
- Cloud deployment

---

## 👩‍💻 Author

**Supriya P**

GitHub: https://github.com/SupriyaCiral

---

## 📄 License

This project is licensed under the MIT License.