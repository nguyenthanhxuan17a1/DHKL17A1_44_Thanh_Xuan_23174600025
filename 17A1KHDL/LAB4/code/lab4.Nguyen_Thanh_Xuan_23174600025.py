import xu_ly_products as xl
def main():
    print("========================")
    print("Menu các chức năng")
    print("1. Hiển thị sản phẩm")
    print("2. Them San Pham")
    print("3. Tim kiem san pham")
    print("4. Cap nhat thong tin san pham")
    print("5. Xoa san pham")
    print("6. Thoat")
    print("=========================")
    while True:
        chon = input("Hay chon chuc nang ban muon: ")
        if chon =='1':
            xl.hien_thi_danh_sach()
        elif chon =='2':
            name = input("nhap ten: ")
            price = float(input("nhap gia: "))
            amount = int(input("nhap so luong: "))
            xl.them_san_pham(name,price,amount)
        elif chon =='3':
            name = input("nhap ten san pham muon tim: ")
            xl.tim_san_pham(name)
        elif chon =='4':
            id = int(input("nhap id san pham: "))
            price = float(input("nhap gia san pham: "))
            amount = int(input("nhap so luong san pham: "))
            xl.cap_nhat_thong_tin(id,price,amount)
        elif chon == '5':
            xl.xoa_san_pham()
        elif chon == '6':
            break
if __name__ == "__main__":
    main()