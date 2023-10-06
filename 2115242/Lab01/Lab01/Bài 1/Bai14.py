from datetime import date
fdate = date(2014, 7, 2)
ldate = date(2014, 7, 11)
soNgay = ldate - fdate
print(f'Số ngày giữa hai khoảng thời gian trên : {soNgay.days}')