so = float(input('Nhập một số bất kì : '))
hieu= so -17
if so>17:
    print(f'Hiệu giữa {so} và 17 là: {hieu*2}')
elif so<17:
    print(f'Hiệu giữa {so} và 17 là: {abs(so-17)}')
else:
    print('Số bạn nhập không hợp lệ!')
