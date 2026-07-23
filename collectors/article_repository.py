import sqlite3

DB_NAME = "database/orion.db"


def save_article_text(article_id, article_text):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE news
        SET article_text = ?
        WHERE id = ?
        """,
        (article_text, article_id),
    )

    conn.commit()
    conn.close()