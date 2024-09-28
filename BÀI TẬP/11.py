import math
class TamGiac:
    def __init__(self, a, b, c):
        self.a = a  
        self.b = b  
        self.c = c  

    def dien_tich(self):
        p = (self.a + self.b + self.c) / 2  
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  

class TamGiacVuong(TamGiac):
    def __init__(self, canh_1, canh_2):
        super().__init__(canh_1, canh_2, math.sqrt(canh_1**2 + canh_2**2))  

class TamGiacCan(TamGiac):
    def __init__(self, canh_khac, canh_bang):
        super().__init__(canh_khac, canh_bang, canh_bang)

class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh)

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
tam_giac = TamGiac(a, b, c)
print(f"Diện tích tam giác: {tam_giac.dien_tich()}")

canh_1 = float(input("Nhập cạnh 1 của tam giác vuông: "))
canh_2 = float(input("Nhập cạnh 2 của tam giác vuông: "))
tam_giac_vuong = TamGiacVuong(canh_1, canh_2)
print(f"Diện tích tam giác vuông: {tam_giac_vuong.dien_tich()}")

canh = float(input("Nhập cạnh của tam giác đều: "))
tam_giac_deu = TamGiacDeu(canh)
print(f"Diện tích tam giác đều: {tam_giac_deu.dien_tich()}")