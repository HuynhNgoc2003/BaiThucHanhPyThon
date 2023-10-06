import calendar
y = int(input("Nhập năm của lịch (yyyy): "))
m = int(input("Nhập tháng của lịch (mm): "))
print(f'''
    Lịch tháng {m} năm {y}
''')
print(calendar.month(y, m))