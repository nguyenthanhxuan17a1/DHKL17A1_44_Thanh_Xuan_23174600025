import sqlite3
conn = sqlite3.connect(r'D:\BÀI TẬP\BÀI TẬP CHƯƠNG 5\data\5.5.db')
cursor = conn.cursor()
cursor.execute("""DELETE FROM hocsinh WHERE id =1""")
rows =cursor.execute("SELECT * FROM hocsinh")
print("Đã xóa hàng  id =1")
conn.commit()
for row in rows:
    print(row)
conn.close()