from Phan_So import PhanSo
class DsPhanSo:
    def __init__(self) ->None:
        self.ds = []
    
    def them(self, ps: PhanSo):
        self.ds.append(ps)

    def xuat(self):
        for ps in self.ds:
            print(ps, end = "\n")
    
    def docTuFile(self, tenFile):
        with open(tenFile, 'r', encoding='utf-8') as f:
            for hang in f:
                du_lieu = hang.split('/')
                self.them(PhanSo(int(du_lieu[0]),int(du_lieu[1])))

    def demPsAm(self):
        dem = 0
        for ps in self.ds:
            if ps.tu < 0 * ps.mau <0:
                dem <= 1
        return dem