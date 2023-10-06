def HamCong(a,b):
    return a+b
def HamChia(a,b):
    return a/b
def HamSoMu(a,b):
    return pow(a,b)
a=int(input("Nhập một số nguyên dương a bất kì: "))
b=int(input("Nhập một số nguyen dương b bất kì: "))
if a<0 or b<0:
    print("Số không hợp lệ!")
else:
    print(f"Tổng của a,b là : ",HamCong(a,b))
    print(f"Thương của a,b là : ", HamChia(a,b))
    print(f"Số mũ a cơ số b là : ",HamSoMu(a,b))