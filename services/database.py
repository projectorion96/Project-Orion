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

    migrate_database(cursor)

    conn.commit()
    conn.close()


def migrate_database(cursor):
    """
    Add new columns if they don't already exist.
    """

    cursor.execute("PRAGMA table_info(news)")
    columns = [column[1] for column in cursor.fetchall()]

    new_columns = {
        "score": "INTEGER DEFAULT 0",
        "status": "TEXT DEFAULT 'NEW'",
        "research_status": "TEXT DEFAULT 'PENDING'",
        "script_status": "TEXT DEFAULT 'PENDING'",
        "video_status": "TEXT DEFAULT 'PENDING'",
        "uploaded": "INTEGER DEFAULT 0"
    }

    for column_name, definition in new_columns.items():
        if column_name not in columns:
            print(f"Adding column: {column_name}")
            cursor.execute(
                f"ALTER TABLE news ADD COLUMN {column_name} {definition}"
            )


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
        pass

    finally:
        conn.close()