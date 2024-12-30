import sqlite3
conn = sqlite3.connect("5.3.db")
curso = conn.cursor()
curso.execute("""CREATE TABLE IF NOT EXISTS nhanvien(
              id INTEGER PRIMARYKEY,
              "Ten" Text,
              "Tuoi" INTEGER)""")
conn.commit()
conn.close()