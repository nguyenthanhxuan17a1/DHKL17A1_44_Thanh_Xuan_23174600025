import sqlite3
conn = sqlite3.connect(':memory:')
print("Đã kết nối tới cơ sở dữ liệu trong bộ nhớ thành công.")
cursor = conn.cursor()
cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT);")
cursor.execute("INSERT INTO test (name) VALUES ('Nguyễn Văn A'), ('Trần Thị B');")
conn.commit()
cursor.execute("SELECT * FROM test;")
rows = cursor.fetchall()
print("Dữ liệu trong bảng 'test':")
for row in rows:
    print(row)
conn.close()