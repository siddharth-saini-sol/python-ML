import math

def func():
    n = 123
    num = n
    count = 0
    while(num > 0):
        last= num %10
        num = num//10
        count=count+1
        print('n',last)
        print(num)
    
    print(count)

def func1():
    n = 1634
    digit = int(math.log10(n)+1)
    num = n 
    res = 0
    while(num>0):
        lastdig = num%10
        res = res+ (lastdig**digit)
        num = num//10
        print(res)
    print(res)

def func2():
    n = 19
    num = 1
    res = []
    while (num <=n):
        if n % num == 0:
            res.append(num)
           # print('num',num)
        num = num +1
        #print(num)
    print(res)

def func3():
    num = 19
    n = int(num**(1/2))
    res = []
    for i in range(1,n+1):
        if num%i==0:
            res.append(i)
            z = num//i
            res.append(z)
    res = set(res)
    res = list(res)
    print(res)
#func()
#func1()
func2()
func3()
print(10%2)
print(36//5)
print(36**(1/2))