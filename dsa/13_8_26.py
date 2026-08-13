def facto():
    lst = []
    A = int(input('enter no'))
    n = int(A**(1/2))
    lst.append(n)
    for i in range(1,(int(A**(1/2)))):
        if (A%i) == 0:
           x = A//i
           lst.append(i)
           lst.append(x)
    print(sorted(lst))
#facto()

def hashmap():
    dic = {}
    lst = [1,1,1,1,1,2,2,2,2,3]
    for i in lst:
        count = 0
        if i not in dic:
            dic[i] = count +1
        else:
            dic[i]=dic[i]+1
        print(dic)
    print(dic) 
#hashmap()
def hashmap2():
    dic = {}
    lst = [1,1,1,1,1,2,2,2,2,3]
    for i in lst:
        dic[i] = dic.get(i,0)+1
    print(dic)
#hashmap2()

def hashmap3():
    n = [5,3,2,2,1,5,5,7,5,10,10,2,67,10,10,111]
    m = [10,111,1,9,5,67,2]
    #{10: 4, 111: 1, 1: 1, 9: 0, 5: 4, 67: 1, 2: 3}
    dic = {}
    dic2 = {}
    for i in n :
        count = 1
        if i not in dic:
            dic[i] = count
        else:
            dic[i] = dic[i]+1
    print(dic)
    dic2 = {}
    for j in m:
        if j in dic:
            dic2[j] = dic[j]
        else:
            dic2[j] = 0
    print(dic2)
