from datetime import datetime

class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self.__maSo
    
    @property
    def hoTen(self):
        return self.__hoTen

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @maSo.setter
    def maSo(self, maSo):
        if self.laMaSoHopLe(maSo):
            self.__maSo = maSo

    @staticmethod
    def laMaSoHopLe(maSo: int):
        return len(str(maSo)) == 7

    @classmethod
    def doiTenTruong(cls, tenmoi):  # Thay self bằng cls
        cls.truong = tenmoi

    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t\t{self.__ngaySinh}"

    def Xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t\t{self.__ngaySinh}")