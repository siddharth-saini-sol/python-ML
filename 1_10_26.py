lst = [55,32,-97,99,3,67]

largest = lst[0]
sec_largest = float("-inf")
n = len(lst)
for i in range(0,n):
    if largest < lst[i]:
        largest = lst[i]
    if lst[i] > sec_largest and lst[i] != largest:
        sec_largest = lst[i]
print(sec_largest)
print(largest)

