import sqlite3
def initialize_database():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    );
    """)
    connection.commit()
    connection.close()

# Hiển thị danh sách sản phẩm
def display_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        print(row)
# Thêm sản phẩm mới
def add_product(name, price,Amount):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO products (name, price, Amount) VALUES (?, ?, ?)", (name, price, Amount))
    connection.commit()
    connection.close()
    print(f"Đã thêm sản phẩm: {name}")

# Tìm kiếm sản phẩm theo tên
def search_product(name):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE name LIKE ?", (f"%{name}%",))
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        print(row)

# Cập nhật đơn giá sản phẩm
def update_price(product_id, new_price):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    connection.commit()
    connection.close()
    print(f"Đã cập nhật đơn giá cho sản phẩm ID {product_id}")

# Xóa sản phẩm theo ID
def delete_product(product_id):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    connection.commit()
    connection.close()
    print(f"Đã xóa sản phẩm ID {product_id}")

# Khởi tạo cơ sở dữ liệu
initialize_database()

# Menu thao tác
while True:
    print("\nQuản lý sản phẩm:")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Tìm kiếm sản phẩm theo tên")
    print("4. Cập nhật đơn giá sản phẩm")
    print("5. Xóa sản phẩm theo ID")
    print("6. Thoát")
    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        display_products()
    elif choice == "2":
        name = input("Nhập tên sản phẩm: ")
        price = float(input("Nhập đơn giá: "))
        quantity = int(input("Nhập số lượng: "))
        add_product(name, price, quantity)
    elif choice == "3":
        name = input("Nhập tên sản phẩm cần tìm: ")
        search_product(name)
    elif choice == "4":
        product_id = int(input("Nhập ID sản phẩm: "))
        new_price = float(input("Nhập đơn giá mới: "))
        update_price(product_id, new_price)
    elif choice == "5":
        product_id = int(input("Nhập ID sản phẩm cần xóa: "))
        delete_product(product_id)
    elif choice == "6":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")
