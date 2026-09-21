lst = [5,7,8,4,1,6,9,2]
for i in range(0,len(lst)):
    for j in range(i,len(lst)):
        if (lst[i] > lst[j]):
            lst[i] , lst[j] = lst[j],lst[i]
        else:
            continue
print(lst)


lst = [5,8,1,6,9,2,4]
for i in range(len(lst)-2,-1,-1):
    for j in range(0 ,len(lst)-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
        else:
            continue
print(lst)