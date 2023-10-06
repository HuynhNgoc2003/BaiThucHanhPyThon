def TimSo(daySo,so):
    for value in daySo:
        if so == value:
            return True
    return False
print(TimSo([1,3,4,6,7,8],7))
print(TimSo([4,7,5,3,9,1],8))