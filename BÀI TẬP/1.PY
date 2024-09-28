class Hinhchunhat:
    def __init__(self):
        self.chieu_dai=float(input("Nhập chiều dài:"))
        self.chieu_rong=float(input("Nhập chiều rộng:"))
    
    def chu_vi(self):
        return 2*(self.chieu_dai+self.chieu_rong)
     
    def dien_tich(self):
        return self.chieu_rong*self.chieu_dai
     
    def in_thong_tin(self):
        print(f'Chiều dài :{self.chieu_dai},Chiều rộng:{self.chieu_rong},Diện tích:{self.dien_tich()},Chu vi:{self.chu_vi()}')
hcn=Hinhchunhat()
hcn.in_thong_tin()