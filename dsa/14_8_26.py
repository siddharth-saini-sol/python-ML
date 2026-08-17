def func():
    s = "azyxyyzaaaa"
    q = ['d','a','y','x']
    dic = {}
    slst = list(s)
    for i in q:
        count = 0
        for j in slst:
            if i==j:
                count =count+1
            dic[i] = count
    print(dic)
#func()

def func1():
    s = "azyxyyzaaaa"
    q = ['d','a','y','x']
    slt = list(s)
    dic = {}
    dic2= {}
    for i in slt:
        dic[i] = dic.get(i,0)+1
    print(dic)
    for j in q:
        count = 0
        if j not in dic:
            dic2[j] = count
        else:
            dic2[j] = dic[j]
    print(dic2)
func1()


        