import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ====== CONFIG ======
folder = "knowledge"  # folder containing .txt files
threshold = 0.25      # similarity threshold
# ====================

# Load .txt files
docs = []
titles = []
for fname in os.listdir(folder):
    if fname.lower().endswith(".txt"):
        path = os.path.join(folder, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                docs.append(content)
                titles.append(fname)

if not docs:
    print("No valid .txt files found in the folder. Exiting...")
    exit()

# Fit TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
tfidf_matrix = vectorizer.fit_transform(docs)

# Console chat loop
print("Gemini Clone ready! Type your question or 'exit' to quit.")
while True:
    query = input("You: ").strip()
    if query.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break
    query_vec = vectorizer.transform([query])
    sims = cosine_similarity(query_vec, tfidf_matrix)[0]
    best_idx = sims.argmax()
    if sims[best_idx] >= threshold:
        print(f"Gemini (from {titles[best_idx]}): {docs[best_idx][:300]}...\n")
    else:
        print("Gemini: Sorry, I don't have an answer for that.\n")