import sqlite3
conn = sqlite3.connect(r'D:\BÀI TẬP\BÀI TẬP CHƯƠNG 5\data\5.5.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS hocsinh (
               id INTEGER PRIMARY KEY,
               'Name' TEXT,
               'Tuoi' INTEGER)""")

cursor.execute("""INSERT INTO hocsinh ('Name','Tuoi') VALUES
               ('Văn',28),('THị',34)""")
conn.commit()
conn.close()