import sqlite3
# Kết nối tới cơ sở dữ liệu (tạo mới nếu không tồn tại)
conn = sqlite3.connect(r'D:\BÀI TẬP\BÀI TẬP CHƯƠNG 5\data\my_data.db')
print("Đã kết nối tới cơ sở dữ liệu thành công.")

# Tạo con trỏ để thực thi câu lệnh SQL
cursor = conn.cursor()

# Lấy phiên bản SQLite
cursor.execute("SELECT sqlite_version();")
version = cursor.fetchone()[0]
print(f"Phiên bản SQLite: {version}")

# Đóng kết nối
conn.close()