import sqlite3

DB_NAME = "database/orion.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
SELECT id, category, title
FROM news
ORDER BY id DESC
""")

rows = cursor.fetchall()

print("=" * 70)
print("PROJECT ORION DATABASE")
print("=" * 70)

for row in rows:
    print(f"{row[0]:<4} {row[1]:<12} {row[2]}")

conn.close()