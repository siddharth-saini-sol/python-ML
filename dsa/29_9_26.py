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
    if len(lst)<=1 :
        return lst
    mid = n//2
    left_arr = lst[:mid]
    right_arr = lst[mid:]
    left = merge_arr(left_arr)
    right = merge_arr(right_arr)
    return merger_sort(left , right)

def merger_sort(left , right):
    res = []
    i,j = 0,0
    n = len(left)
    m = len(right)
    while(i<n and j<m) :
        if (left[i] <= right[j]):
            res.append(left[i])
            i=i+1
        else:
            res.append(right[j])
            j=j+1
    while (i<n):
        res.append(left[i])
        i=i+1
    while(j<m):
        res.append(right[j])
        j=j+1
    return res
main_res = merge_arr(lst)
print(main_res)
