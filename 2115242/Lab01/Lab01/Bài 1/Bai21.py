def LaSoChan(num:int):
    return num%2==0
num=int(input("Nhập vào một số bất kỳ: "))
if LaSoChan(num):
    print("Số vừa nhập là số chẵn")
else:
    print("Số vừa nhập là số lẻ")