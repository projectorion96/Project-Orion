import sqlite3


def get_top_story():

    conn = sqlite3.connect("database/orion.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, category
        FROM news
        ORDER BY score DESC
        LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0], row[1]

    return None