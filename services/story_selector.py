import sqlite3
import re

DB_NAME = "database/orion.db"

KEYWORDS = {
    "OpenAI": 30,
    "GPT": 30,
    "AI": 25,
    "Artificial Intelligence": 25,
    "Microsoft": 20,
    "Google": 20,
    "Meta": 20,
    "NVIDIA": 25,
    "Anthropic": 25,
    "Apple": 15,
    "Tesla": 15,
    "Amazon": 15,
    "Cyber": 10,
    "Security": 10,
}


def calculate_score(title):
    score = 0

    # Split title into words so "AI" doesn't match inside other words
    words = re.findall(r"\b[\w.-]+\b", title.lower())

    for keyword, points in KEYWORDS.items():
        keyword_words = keyword.lower().split()

        if len(keyword_words) == 1:
            if keyword.lower() in words:
                score += points
        else:
            if keyword.lower() in title.lower():
                score += points

    return score


conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
SELECT category,title
FROM news
""")

articles = cursor.fetchall()

best_score = -1
best_article = None

for article in articles:

    score = calculate_score(article[1])

    if score > best_score:
        best_score = score
        best_article = article

print("=" * 70)
print("PROJECT ORION - TOP STORY")
print("=" * 70)

print(f"Category : {best_article[0]}")
print(f"Score    : {best_score}")
print()
print(best_article[1])

conn.close()