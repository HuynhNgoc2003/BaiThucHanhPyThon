def Chuoi_copy(text,n):
    flen = 2
    if flen>len(text):
        flen=len(text)
    ChuoiDuocLay=text[:flen]
    result=""
    for i in range(n):
        result= result+ChuoiDuocLay
    return result
print(Chuoi_copy("Bacdefj",3))
print(Chuoi_copy("Mamimo",2))
print(Chuoi_copy("E",7))