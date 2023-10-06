def XuatCacSoLeChiaHetCho5(so: int):
    if (so % 2 != 0 and so % 5 == 0):
        return True
    return False

def KTrFibonacci(n):
    if n <= 0:
        return False
    elif n == 1:
        return False
    else:
        return KTrFibonacci(n-1) + KTrFibonacci(n-2)


day = [1,2,3,4,5,6,7,8,9,10]
day_moi = list(filter(XuatCacSoLeChiaHetCho5, day))
print(day_moi)
day_Fibo = list(filter(KTrFibonacci, day))
print(day_Fibo)