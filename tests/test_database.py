import sqlite3

conn = sqlite3.connect("database/orion.db")
cursor = conn.cursor()

print("\n=== NEWS TABLE STRUCTURE ===")
cursor.execute("PRAGMA table_info(news)")
for column in cursor.fetchall():
    print(column)

print("\n=== TOTAL ARTICLES ===")
cursor.execute("SELECT COUNT(*) FROM news")
print(cursor.fetchone()[0])

conn.close()