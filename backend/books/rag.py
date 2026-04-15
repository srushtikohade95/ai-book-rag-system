import pandas as pd
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

print("Setting file paths...")
BOOKS_PATH = "books.csv"
EMBEDDINGS_PATH = "embeddings.pkl"

print("Loading data...")
df = pd.read_csv(BOOKS_PATH)

with open(EMBEDDINGS_PATH, "rb") as f:
    embeddings = pickle.load(f)


def generate_summary(text):
    if not isinstance(text, str) or text.strip() == "":
        return "No description available"
    return text[:150] + "..."


def generate_answer(query):
    print("Processing query...")

    query_embedding = model.encode([query])

    similarities = np.dot(embeddings, query_embedding.T).flatten()

    # ✅ Get top 3 books
    top_indices = np.argsort(similarities)[-3:][::-1]

    response = f'Based on your query: "{query}"\n\nHere are some recommended books:\n\n'

    for idx in top_indices:
        book = df.iloc[idx]

        summary = generate_summary(book['description'])

        response += f"""
Book Title: {book['title']}
Author: {book['author']}
Summary: {summary}
Description: {book['description']}

-------------------------
"""

    return response