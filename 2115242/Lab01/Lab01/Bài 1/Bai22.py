def Ham_Tim_4(dayso):
    count=0
    for so in dayso:
        if so==4:
            count=count+1
    return count
print(Ham_Tim_4([1,3,4,5,4,4]))
print(Ham_Tim_4([7,4,3,4,5,4,4]))