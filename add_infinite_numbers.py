def sum(a,b,*c):
    lst = []
    for i in c:
        lst.append(i)
    tem = 0
    for j in lst:
        tem = tem + j
    return a+ b + tem
print(sum(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))



