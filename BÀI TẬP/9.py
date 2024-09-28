class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh

    def chu_vi(self):
        pass  

    def dien_tich(self):
        pass  

class HinhBinhHanh(DaGiac):
    def __init__(self, day, chieu_cao):
        super().__init__(4)  
        self.day = day
        self.chieu_cao = chieu_cao

    def chu_vi(self):
        return 2 * (self.day + self.chieu_cao)

    def dien_tich(self):
        return self.day * self.chieu_cao

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, rong, cao):
        super().__init__(rong, cao)

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh) 

day_binh_hanh = float(input("Đáy hình bình hành: "))
chieu_cao_binh_hanh = float(input("Chiều cao hình bình hành: "))
hinh_binh_hanh = HinhBinhHanh(day_binh_hanh, chieu_cao_binh_hanh)
print(f"Hình bình hành - Chu vi: {hinh_binh_hanh.chu_vi()}, Diện tích: {hinh_binh_hanh.dien_tich()}")

rong_chu_nhat = float(input("Chiều rộng hình chữ nhật: "))
cao_chu_nhat = float(input("Chiều cao hình chữ nhật: "))
hinh_chu_nhat = HinhChuNhat(rong_chu_nhat, cao_chu_nhat)
print(f"Hình chữ nhật - Chu vi: {hinh_chu_nhat.chu_vi()}, Diện tích: {hinh_chu_nhat.dien_tich()}")

canh_hinh_vuong = float(input("Cạnh hình vuông: "))
hinh_vuong = HinhVuong(canh_hinh_vuong)
print(f"Hình vuông - Chu vi: {hinh_vuong.chu_vi()}, Diện tích: {hinh_vuong.dien_tich()}")