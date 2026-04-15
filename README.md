# 📚 AI Book Query System (RAG)

## Overview

This project is a backend-based AI Book Query System built using Django REST Framework. It collects book data, stores it, and allows users to query the data using a simple RAG (Retrieval-Augmented Generation) approach.

The main idea is to combine data scraping with intelligent querying so that users can get meaningful insights about books.

---

## Features

* Scrapes book data from the web
* Stores book details in a database
* Provides APIs to fetch all books and individual book details
* Recommends related books
* Supports question-answering using a basic RAG pipeline
* Generates simple AI-based insights like:

  * Summary
  * Genre classification
  * Sentiment analysis

---

## Tech Stack

* Python
* Django REST Framework
* SQLite (database)
* Basic embedding + retrieval logic
* Git & GitHub

---

## Project Structure

```
book-ai-project/
│
├── backend/
│   ├── books/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── scraper.py
│   │   ├── rag.py
│   │
│   ├── manage.py
│   ├── requirements.txt
│   ├── books.csv
│   ├── embeddings.pkl
│
└── README.md
```

---

## How to Run

1. Clone the repo:

```
git clone https://github.com/srushtikohade95/ai-book-rag-system.git
```

2. Go to backend:

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

## API Endpoints

* `/api/all/` → get all books
* `/api/book/<id>/` → get book details
* `/api/book/<id>/recommend/` → get similar books
* `/api/scrape/` → scrape and store data
* `/api/ask/` → ask questions about books

---

## Example

```
http://127.0.0.1:8000/api/ask/?q=python
```

---

## Screenshots / Output

Screenshots showing working APIs and outputs are attached for reference.

---
<img width="1281" height="879" alt="image" src="https://github.com/user-attachments/assets/9ba17e41-5b5f-4655-9028-5362f37115f9" />
<img width="1760" height="990" alt="image" src="https://github.com/user-attachments/assets/5a160446-cf45-438c-b147-8c29e41ee885" />
<img width="1760" height="990" alt="image" src="https://github.com/user-attachments/assets/72ffb088-4db2-4e84-8bc3-c092187736d6" />
<img width="1760" height="990" alt="image" src="https://github.com/user-attachments/assets/3ab99d16-ab2d-4592-82b1-8dc4593adba5" />
<img width="1760" height="990" alt="image" src="https://github.com/user-attachments/assets/01144f98-398d-47ea-bfd9-d2560d0e36c2" />
<img width="1760" height="990" alt="image" src="https://github.com/user-attachments/assets/c5ba1a30-620d-497f-a527-0a0e2b2f5273" />
<img width="1760" height="990" alt="image" src="https://github.com/user-attachments/assets/33c09670-0df6-421e-b73e-27ebf155e0e0" />
<img width="1760" height="990" alt="image" src="https://github.com/user-attachments/assets/06cbf3d5-dca0-4b27-9471-cc49dd5f7041" />
<img width="1760" height="990" alt="image" src="https://github.com/user-attachments/assets/2b9f7335-c431-4e57-b43f-8b89883ee2c7" />
<img width="1760" height="990" alt="image" src="https://github.com/user-attachments/assets/bc093ce2-8ab1-41de-a406-5038cf636ab0" />
<img width="1760" height="990" alt="image" src="https://github.com/user-attachments/assets/ed6058e8-a1ce-445b-ad2e-551af37db273" />


## Note

* The backend is fully functional and tested.
* Frontend part is not completed due to time constraints.
* Focus has been on backend logic, APIs, and AI-based querying.

---

## Author

Srushti Kohade
