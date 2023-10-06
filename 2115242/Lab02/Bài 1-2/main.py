from SinhVien import SinhVien
from dssv import DanhSachSv
import datetime

ds = DanhSachSv()
ds.docTuFile('C:\\Users\\Admin\\Desktop\\2115242\\Lab02\Bài 1-2\\dssv.txt')
ds.Xuat()

ds.themSV()
ds.Xuat()

print("1. Tìm sv theo mssv")
ma = int(input("Nhập MSSV: "))
kq = ds.timSinhVienTheoMssv(ma)
if kq>0:
    print(f"Sinh viên có MSSV {ma} là: ")
    for sv in kq:
        print(sv)
else:
        print(f"Không tìm thấy sinh viên có MSSV {ma}")
    
print("2. Tìm sv theo tên")
ten = input("Nhập tên: ")
kq = ds.timSvTheoTen(ten)
if kq>0:
    print(f"Sinh viên có tên {ten} trong danh sách là:")
for sv in kq:
    print(sv)
else:
    print(f"Không tìm thấy sinh viên có tên: {ten}")

print("3. Xóa sinh viên theo MSSV")
ma = int(input("Nhập MSSV: "))
if ds.XoaSvTheoMssv(ma):
    print(f"Xóa sinh viên MSSV {ma}")
    ds.Xuat()
else:
    print(f"Không tìm thấy sinh viên có MSSV {ma} để xóa")
    
print("4. Tìm sinh viên sinh trước ngày")
ngay = datetime (2000, 1, 1)
kq = ds.timSvSinhTruocNgay(ngay)

if kq>0:
    print(f"Sinh viên sinh trước ngày {ngay.strftime('%d/%m/%Y')}:")
for sv in kq:
    print(sv)
else:
    print(f"Không có sinh viên nào sinh trước ngày {ngay.strftime('%d/%m/%Y')}")
    
print("5. Tìm vị trí sinh viên theo MSSV")
masv = int(input("Nhập MSSV: "))
vt = ds.timVTSvTheoMssv(masv)

if vt != -1:
    print(f"Sinh viên có MSSV {masv} tại vị trí {vt + 1}")
else:
    print(f"Không tìm thấy sinh viên với MSSV {masv}")