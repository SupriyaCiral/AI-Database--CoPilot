# 🤖 AI Database Copilot

An AI-powered Database Copilot built using **FastAPI**, **Ollama**, **SQLAlchemy**, and **SQLite**. The application converts natural language questions into SQL queries, validates them for safety, executes them against a database, and returns the results.

---

## 🚀 Features

- 🤖 AI-powered Natural Language to SQL generation
- 🗄️ SQLite database integration using SQLAlchemy ORM
- 🔍 Automatic database schema discovery
- 🛡️ SQL query validation before execution
- ⚡ FastAPI REST API
- 📜 Chat history storage
- 🐳 Dockerized application
- 📖 Interactive Swagger API documentation

---

## 🏗️ Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- Ollama (Llama 3)
- Pydantic
- HTTPX
- Docker

---

## 📂 Project Structure

```text
AI-Database-Copilot/
│
├── app/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── services/
│   ├── config.py
│   └── main.py
│
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/AI-Database-Copilot.git

cd AI-Database-Copilot
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment

Create a `.env` file

```env
OLLAMA_BASE_URL=http://localhost:11434
MODEL_NAME=llama3:8b
```

---

### Start Ollama

```bash
ollama serve
```

Download model

```bash
ollama pull llama3:8b
```

---

### Run Application

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

---

# 🐳 Docker

Build Docker Image

```bash
docker build -t ai-database-copilot .
```

Run Container

```bash
docker run -p 8000:8000 \
-e OLLAMA_BASE_URL=http://host.docker.internal:11434 \
ai-database-copilot
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Health Check |
| POST | /ask | Ask AI |
| GET | /tables | List database tables |
| POST | /generate-sql | Generate SQL from natural language |

---

## Future Enhancements

- Multi-table support
- PostgreSQL integration
- Role-based authentication
- Query execution history
- Google Cloud deployment
- CI/CD using GitHub Actions
- Docker Compose
- Kubernetes deployment
- College ERP AI Assistant

---

## Author

**Supriya P**

Assistant Professor | AI & Software Engineering

---

## License

MIT License