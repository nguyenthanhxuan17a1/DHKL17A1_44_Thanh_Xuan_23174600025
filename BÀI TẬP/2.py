class TS:
    def __init__(self):
        self.ho_ten=input("Nhập họ và tên:")
        self.toan=float(input("Nhập điểm toán:"))
        self.hoa=float(input("Nhập điểm hóa :"))
        self.ly=float(input("Nhập điểm lí:"))
    
    def tong_diem(self):
        return self.toan+self.hoa+self.ly
                       
    def in_thong_tin(self):
        print(f"{self.ho_ten}:Tổng điểm:{self.tong_diem()}")

danh_sach = [TS() for i in range(int(input("Số lượng thí sinh: ")))]
danh_sach_trung_tuyen = sorted([ts for ts in danh_sach if ts.tong_diem()>= 20], key=lambda x: x.tong_diem(), reverse=True)
print("\nDanh sách thí sinh trúng tuyển:")
for ts in danh_sach_trung_tuyen:
    ts.in_thong_tin()

