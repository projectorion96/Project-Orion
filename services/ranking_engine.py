import sqlite3

DB_NAME = "database/orion.db"

# Keywords that increase the score
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

    for keyword, points in KEYWORDS.items():
        if keyword.lower() in title.lower():
            score += points

    return score


def rank_articles():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, category, title
        FROM news
    """)

    articles = cursor.fetchall()

    ranked = []

    for article in articles:

        article_id = article[0]
        category = article[1]
        title = article[2]

        score = calculate_score(title)

        # Save score into database
        cursor.execute(
            "UPDATE news SET score=? WHERE id=?",
            (score, article_id)
        )

        ranked.append((score, category, title))

    conn.commit()

    ranked.sort(reverse=True)

    print("=" * 80)
    print("PROJECT ORION - TOP STORIES")
    print("=" * 80)

    for score, category, title in ranked:
        print(f"Score: {score:3} | {category:12} | {title}")

    conn.close()


if __name__ == "__main__":
    rank_articles()