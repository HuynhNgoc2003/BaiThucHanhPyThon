def ChuoiMoi(txt):
    if len(txt)>= 2 and txt [:2]=="Is":
        return txt
    return "Is"+ txt
print(ChuoiMoi("IsEmpty"))
print(ChuoiMoi("Sample"))