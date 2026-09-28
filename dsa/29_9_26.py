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


#merge sort 
def merge_arr(lst):
    n = len(lst)
    if len(lst) <= 1:
        return lst
    mid = n//2
    left_arr = lst[:mid]
    right_arr = lst[mid:]
    left = merge_arr(left_arr)
    rigth = merge_arr(rigth_arr)
    return merger_sort(left , rigth)

def merger_sort(left , right):
    res = []
    i,j = 0
    n,m = len(left) , len(right) 
    while(i<n and j<m) :
        if (left[i] <= rigth[j]):
            res.append(left[i])
            i++
        else:
            res.append(rigth[j])
            j++
    if (i<n) :
        while(i<n):
            res.append(left[i])
            i++
    if(j<m):
        while(j<m):
            res.append(rigth[j])
            j++
    return res
