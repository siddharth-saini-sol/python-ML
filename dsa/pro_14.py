strs = ['flower','flow','flight']
"""
strs = sorted(strs)
print(strs)
lst  = []
for i in range(0,len(strs)-2):
    print('i=',i)
    for j in strs[i]:
        if j in strs[i+1]:
            lst.append(j)
print(lst)
flst = []
isfound = 0
for i in lst:
    if i in strs[-1]:
        flst.append(i)
        isfound = 1
    else:
        break
        isfound = 0
    
print(flst)
---------------------------

lst = []
flst = []
slst = []
for i in strs:
    x = list(i)
    lst.append(x)
print(lst)
for i in range(0,len(lst)-1):
    for j in lst[i]:
        if j in lst[i+1]:
            flst.append(j)

"""
"""
import statistics
lst= []
for i in strs[0:]:
    for j in i:
        lst.append(ord(j))
x = statistics.multimode(lst)
import statistics
lst = []
flst = []
for i in strs:
    x = list(i)
    for i in x:
        lst.append(ord(i))
x = statistics.multimode(lst)
for i in x:
    flst.append(chr(i))
print("".join(flst))
"""
    
strs = ['flower','flight','flow']
ref = strs[0]
print(ref)
strs.remove(ref)
print(strs)
for i in strs:
    for j in range(len(i)):
        if i[j] == ref[j]:
            print(i[j])
        else:
            break

        
