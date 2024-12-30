import sqlite3
conn = sqlite3.connect(r'D:\BÀI TẬP\BÀI TẬP CHƯƠNG 5\data\5.3.db')
curso = conn.cursor()
curso.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = curso.fetchall()
for rows in tables:
    print(rows)

conn.close()