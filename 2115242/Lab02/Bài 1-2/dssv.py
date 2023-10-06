from SinhVien import SinhVien
import datetime
class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
    
    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def Xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSinhVienTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.mssv == mssv]
    
    def timVTSvTheoMssv(self, mssv:int):
        for i in range (len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1

    def docTuFile(self, tenFile):
        with open(tenFile, 'r', encoding='utf-8') as f:
            for hang in f:
                du_lieu = hang.split(',')
                self.themSV(SinhVien(int(du_lieu)))

    def XoaSvTheoMssv(self, maso:int) -> bool:
        vt = self.timSinhVienTheoMssv(maso)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
        
    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.ten == 'Nam']

    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngay <= '15/06/2000']
    
    def sapxepTheoTenTD(self,ten: str):
        tangdan = self.dssv.sort(key=lambda self: self._ten, reverse=False)
        return tangdan