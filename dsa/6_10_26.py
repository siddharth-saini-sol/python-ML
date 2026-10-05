lst = [1,2,3,4,5,6,7,8]
k = 4
end = len(lst) - k
for i in range(0,k):
    for j in range(len(lst)-1,end-1,-1):  #(7,6,-1)
        lst[i],lst[j]=lst[j],lst[i]
print(lst)

temp = lst[0]
for i in range(len(lst)-2,-1,-1):
    lst[i+1]=lst[i]
lst[0] = temp
print(lst)

