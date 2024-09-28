import math

class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)  
        self.a = a  
        self.b = b  

    def dien_tich(self):
        return math.pi * self.a * self.b  

class DuongTron(Elip):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r)  
        self.r = r  # Bán kính

    def dien_tich(self):
        return math.pi * self.r ** 2  

x_elip = float(input("Nhập tọa độ x của tâm elip: "))
y_elip = float(input("Nhập tọa độ y của tâm elip: "))
ban_truc_lon = float(input("Nhập bán trục lớn (a): "))
ban_truc_nho = float(input("Nhập bán trục nhỏ (b): "))

elip = Elip(x_elip, y_elip, ban_truc_lon, ban_truc_nho)
print(f"Diện tích elip: {elip.dien_tich()}")

x_duong_tron = float(input("Nhập tọa độ x của tâm đường tròn: "))
y_duong_tron = float(input("Nhập tọa độ y của tâm đường tròn: "))
ban_kinh = float(input("Nhập bán kính (r): "))

duong_tron = DuongTron(x_duong_tron, y_duong_tron, ban_kinh)
print(f"Diện tích đường tròn: {duong_tron.dien_tich()}")