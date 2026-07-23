import sqlite3

DB_NAME = "database/orion.db"


def get_top_story():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title,
               category,
               article_text
        FROM news
        ORDER BY score DESC
        LIMIT 1
    """)

    story = cursor.fetchone()

    conn.close()

    return story