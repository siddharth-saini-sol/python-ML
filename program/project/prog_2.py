arr=[23, 87, 15, 64, 91, 42, 8, 56, 77, 31]
largest = float('-inf')
second = float('-inf')

for num in arr:
    if num > largest:
        second = largest 
        largest = num 
    elif num > second and num != largest:
        second = num
        
print(largest)
print(second)

import numpy as np 

arr = np.array([1,2,3,4,5,6])
print(arr.reshape(-1,1))