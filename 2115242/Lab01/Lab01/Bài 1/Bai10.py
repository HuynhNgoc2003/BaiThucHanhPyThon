a = int(input("Nhập 1 số nguyên n bất kì : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
S= n1+n2+n3
print (f"Tổng n+nn+nnn là : {S}" )