import sqlite3

DB_NAME = "database/orion.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        title TEXT,
        link TEXT UNIQUE,
        published TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_news(category, title, link, published):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO news(category,title,link,published)
            VALUES(?,?,?,?)
        """, (category, title, link, published))

        conn.commit()

    except sqlite3.IntegrityError:
        # Duplicate article
        pass

    finally:
        conn.close()