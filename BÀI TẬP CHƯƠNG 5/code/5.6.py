import sqlite3 
conn= sqlite3.connect(r'D:\BÀI TẬP\BÀI TẬP CHƯƠNG 5\data\5.5.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM hocsinh")
rows =cursor.fetchall()
print("Danh sách các bản ghi trong bảng 'hocsinh':")
for row in rows:
    print(row)
conn.close()