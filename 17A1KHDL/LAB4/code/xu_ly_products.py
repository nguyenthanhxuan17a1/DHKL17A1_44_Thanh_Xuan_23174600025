import sqlite3
conn = sqlite3.connect(r'.\LAB4\data\product.db')
cruso = conn.cursor()
cruso.execute("""CREATE TABLE IF NOT EXISTS product(
              id INTEGER PRIMARY KEY,
              'Name' Text Not null,
              'Price' Real Not null,
              'Amount' Interger Not Null)""")


def hien_thi_danh_sach():
    rows = cruso.execute("SELECT * FROM product")
    for row in rows:
        print(row)

def them_san_pham(name,price,amount):
    cruso.execute("INSERT INTO product('Name','Price','Amount') VALUES(?,?,?)",(name,price,amount))
    conn.commit()
    print('Đã thêm sản phẩm')

def tim_san_pham(name):
    rows =cruso.execute("SELECT * FROM product WHERE Name = ?",(name,))
    for row in rows:
        print(row)
def cap_nhat_thong_tin(id,price,amount):
    cruso.execute("UPDATE product SET Price = ?, Amount =? WHERE id = ?",(price,amount,id))
    conn.commit()
    return f'Đã cập nhật thông tin'
def xoa_san_pham():
    id = int(input("Nhập tên sản phẩm muốn xóa "))
    cruso.execute("DELETE FROM product WHERE id = ?",(id,))
    conn.commit()
    print("Đã xóa sản phẩm")