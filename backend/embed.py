import pandas as pd
from sentence_transformers import SentenceTransformer
import pickle

print("Loading CSV...")
df = pd.read_csv("books.csv")

print("Loading model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

print("Preparing text...")
df['text'] = df['title'] + " " + df['author'] + " " + df['description']

print("Creating embeddings...")
embeddings = model.encode(df['text'].tolist())

print("Saving files...")
with open("embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)

df.to_pickle("books.pkl")

print("✅ DONE")