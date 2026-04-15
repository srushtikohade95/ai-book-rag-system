# 📚 AI Book RAG System

## 🔍 Overview

This project is an AI-powered Book Query System built using Django and Retrieval-Augmented Generation (RAG). It allows users to retrieve relevant book information and ask queries based on stored data.

---

## ⚙️ Features

* 📖 Book data scraping
* 🔍 Search and retrieval of books
* 🤖 AI-based query answering (RAG)
* 🌐 REST API endpoints

---

## 🛠️ Tech Stack

* Python
* Django
* Pandas
* Pickle (for embeddings)
* REST APIs

---

## 📂 Project Structure

```
backend/
│
├── books/            # App for book logic
├── manage.py         # Django entry point
├── requirements.txt  # Dependencies
├── books.csv         # Book dataset
├── embeddings.pkl    # Precomputed embeddings
```

---

## 🚀 How to Run

1. Clone the repo:

```
git clone https://github.com/srushtikohade95/ai-book-rag-system.git
```

2. Navigate to project:

```
cd ai-book-rag-system/backend
```

3. Create virtual environment:

```
python -m venv venv
```

4. Activate:

```
venv\Scripts\activate
```

5. Install dependencies:

```
pip install -r requirements.txt
```

6. Run server:

```
python manage.py runserver
```

---

## 🔗 API Endpoints

* `/api/all/` → Get all books
* `/api/scrape/` → Scrape book data
* `/api/ask/` → Ask queries
* `/api/book/<id>/` → Get book by ID

---

## 💡 Example Query

```
http://127.0.0.1:8000/api/ask/?query=python
```

---

## 📌 Note

This is a development project and runs on Django's local server.

---

## 👩‍💻 Author

Srushti Kohade
