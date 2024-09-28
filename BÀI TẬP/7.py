class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def in_thong_tin(self):
        print(f"Ngày: {self.day}/{self.month}/{self.year}")

    def nam_nhuan(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    def ngay_trong_thang(self, month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if self.nam_nhuan(year) else 28
        return 0

    def next(self):
        if self.day < self.ngay_trong_thang(self.month, self.year):
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

date = Date(28, 2, 2024) 
date.in_thong_tin() 
date.next() 
date.in_thong_tin()
  

