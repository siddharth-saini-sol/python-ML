from math import *
def armg(n):
    num = n 
    res = 0
    cnt = 0 
    numop= n
    count = int(log10(n)+1)
    while(num>0):
        lst = num%10
        res = (res*10)+lst
        num = num//10
        cnt = (lst**count) + cnt
    if numop == cnt:
        return True
    else:
        return False
print(armg(1634))


def fact(n):
    num =n 
    lst = []
    #lst.append(n)
    if num%2==0:
        lst.append(2)
    for i in range(1,num,2):
        if num%i==0:
            lst.append(i)
    lst.append(n)
    print(lst)
fact(7)