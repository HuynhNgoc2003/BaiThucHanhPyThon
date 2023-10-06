def HamTinhDienTichHCN(a,b):
    return a*b
a=int(input("Nhập chiều dài: "))
b=int(input("Nhập chiều rộng: "))
if a<0 or b<0:
    print("Số không hợp lệ!")
else:
    print(f"Diện tích hình chữ nhật là : ",HamTinhDienTichHCN(a,b))

