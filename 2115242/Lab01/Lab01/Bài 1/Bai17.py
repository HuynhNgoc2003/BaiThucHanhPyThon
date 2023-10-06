def near_thousand(n):
    return ((abs(1000-n)<=100)or(abs(2000-n)<=100))
print(near_thousand(999))
print(near_thousand(33))
print(near_thousand(1440))
print(near_thousand(2500))