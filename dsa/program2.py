def func():
    num = [5,6,7,7,1,9,111,1,1,1,5,1]
    dic = {}
    num_set = set(num)
    for i in num_set:
        count = 0
        for j in range(len(num)):
           # print(f'i,{i} and j,{j} ele {num[j]}')
            if i == num[j]:
                count=count+1
            dic[i] = count
        
    print(dic)

func()

def func2():
    dic = {}
    num = [5,6,7,7,1,9,111,1,1,1,5,1,6,0,0,0,0,0,0]
    count = 1
    for i in num:
        if i not in dic:
            dic[i] = 1
            continue
        else:
            dic[i]+=1
        #continue
    print(dic)
        
func2()

def func3():
    dic = {}
    num = [5,6,7,7,1,9,111,1,1,1,5,1,6,0,0,0,0,0,0]
    for i in num :
        dic[i] = dic.get(i,0)+1
        print(dic)
    print(dic)
func3()

def func4():
    dic = {}
    n = [5,3,2,2,1,5,5,7,5,10]
    m = [10,111,1,9,5,67,2]
    for i in m:
        count = 0
        for j in n:
            if i == j:
                count=count+1
            dic[i] = count
        print(dic)

    
    dic = {}
    n = [5,3,2,2,1,5,5,7,5,10]
    m = [10,111,1,9,5,67,2]
    for i in n :
        dic[i] = dic.get(i,0)+1
        print(dic)
    dic2 = {}
    dic3={}
    for j in m :
        if j in dic:
            dic2[j] = dic[j]
        else:
            dic2[j] = 0
        print(dic2)
func4()

def func5():
    s = "azyxyyzaaaa"
    q = ["d","a","q","x"]
    dic = {}
    dic2 = {}
    lst = list(s)
    #lst = ['a', 'z', 'y', 'x', 'y', 'y', 'z', 'a', 'a', 'a', 'a']
    for i in lst:
        dic[i] = dic.get(i,0)+1
    print(dic)
    for j in q :
        if j in dic:
            dic2[j] = dic[j]
        else:
            dic2[j] = 0
        print(dic2[j])
 
    s = "azyxyyzaaaa"
    q = ["d","a","q","x"]
    lst = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,00,0]
    for i in s:
        ascii_val = ord(i) - 97
        lst[ascii_val] = lst[ascii_val]+1
    print(lst)

func5()

n = -121
num = n
res = 0
while(num>0):
    ls = num%10
    res=(res*10)+ls
    num = num//10
print(res)
print(num)
ispal = False
if res == n:
    ispal = True
    print(ispal)
else:
    print(ispal)