import math

class PS:
    def __init__(self,tu_so=0,mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.rut_gon()

    def hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        if not self.hop_le():
            print("Mẫu số không được bằng 0!")
            self.nhap_phan_so()
        self.rut_gon()

    def in_phan_so(self):
        print(f"{self.tu_so}/{self.mau_so}")

    def rut_gon(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln
        if self.mau_so < 0:
            self.tu_so, self.mau_so = -self.tu_so, -self.mau_so

ps = PS()
ps.nhap_phan_so()
ps.in_phan_so()
