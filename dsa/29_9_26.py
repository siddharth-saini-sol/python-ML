lst = [3,5,6,4,8,9,10,7,1]
n = len(lst)
for i in range(0,n):
    key = lst[i]
    j = i-1
    while(j>=0 and lst[j] > key):
        lst[j+1] = lst[j]
        j=j-1
    lst[j+1] = key
print(lst)