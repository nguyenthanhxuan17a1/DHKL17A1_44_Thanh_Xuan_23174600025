import sqlite3
conn = sqlite3.connect(r'D:\BÀI TẬP\BÀI TẬP CHƯƠNG 5\data\5.5.db')
cursor = conn.cursor()
cursor.execute("""UPDATE hocsinh SET 'Tuoi' = 19""")
row =cursor.execute("SELECT * FROM hocsinh")
conn.commit()
for rows in row:
    print(rows)
conn.close()