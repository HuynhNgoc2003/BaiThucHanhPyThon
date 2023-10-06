import math
class PhanSo:
    def __init__(self, tu=1, mau=1) -> None:
        if mau == 0:
            print("Mẫu số không thể bằng 0")
        self.tu = tu
        self.mau = mau

    def __str__(self) -> str:
        return str(self.tu//self.mau) if self.tu % self.mau == 0 else "{}/{}".format(self.tu,self.mau)
    
    def __add__(self, other):
        ps = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        ps.tu = self.tu*other.mau + self.mau*other.tu
        ps.mau = self.mau + other.mau
        return ps.rutGon()
    
    def rutGon(self):
        ps = PhanSo()
        ucln = math.gcd(self.tu, self.mau)
        ps.tu = self.tu/ucln
        ps.mau = self.mau/ucln
        return ps
    
    def __sub__(self, other):
        ps = PhanSo()
        ps.tu = self.tu * other.mau - self.mau * other.tu
        ps.mau = self.mau * other.mau
        ps.rutGon()
        return ps
    
    def __mul__(self, other):
        ps = PhanSo()
        ps.tu = self.tu * other.tu
        ps.mau = self.mau * other.mau
        ps.rutGon()
        return ps

    def __truediv__(self, other):
        ps = PhanSo()
        ps.tu = self.tu * other.mau
        ps.mau = self.mau * other.tu
        ps.rutGon()
        return ps


























