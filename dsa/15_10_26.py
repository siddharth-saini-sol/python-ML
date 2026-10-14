n1 = [1,1,1,1,2,3,4,6,7]
n2 = [1,2,3,6,7,8,9]
lst = n1+n2 
lst = list(set(lst))
print(lst)


i=0
j=0
lst = []
while (i<len(n1) and j<len(n2)):
    if n1[i] <= n2[j]:
        if len(lst) ==0 or lst[-1]!= n1[i] :
            lst.append(n1[i])
        i=i+1
    else:
        if  len(lst) == 0 or lst[-1]!= n2[j]:
            lst.append(n2[j])
        j=j+1
while j<len(n2):
    if  len(lst) == 0 or lst[-1]!= n2[j]:
        lst.append(n2[j])
    j=j+1
while i<len(n1):
    if len(lst) ==0 or lst[-1]!=n1[i]:
        lst.append(n1[i])
    i=i+1
print(lst)
        

