import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

df = pickle.load(open("books.pkl", "rb"))
embeddings = pickle.load(open("embeddings.pkl", "rb"))

query = input("Ask something: ")

query_embedding = model.encode([query])
scores = np.dot(embeddings, query_embedding.T).flatten()

top_index = np.argmax(scores)

print("\nBest Match:")
print(df.iloc[top_index])