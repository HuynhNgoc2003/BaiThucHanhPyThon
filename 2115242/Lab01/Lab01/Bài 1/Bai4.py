from math import PI

def TinhDienTichHinhTron(banKinh:float):
if banKinh>=0:
    S= PI*banKinh**2
    return S

banKinh = float(input('Nhập bán kính r : '))
if banKinh>=0:
    S = TinhDienTichHinhTron(banKinh)
    print (f'Diện tích hình tròn với bán kính {banKinh} là : {S}')
else:
    print('Bán kính không hợp lệ!')