"""
lst = [1,2,3,4,5,6,3,7]
n = len(lst)
count = 0
for i in range(0,n-1):
    if lst[i] <= lst[i+1]:
        continue
    else:
        count = count+1
if (count!=0): 
    print('false')
else:
    print('true')
"""
        
lst = [1,1,2]
set_lst = list(set(lst))
#print(set_lst)

le1 = len(lst) #12
#print(le1)
lst = list(set(lst)) 
#print(len(lst))
le2 = len(lst) #4
x = le1-le2  #8
#print(x)
for i in range(0,x):   #range(0,8)
    lst.append('_')
print(lst)
print(le2)