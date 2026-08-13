"""
nums = [1,2,3,1]
k = 3
found = False
for i in range(len(nums)):
    for j in range(len(nums)-1,-1,-1):
        if i!=j:
            #print(f"i:{i} num {nums[i]} and j:{j} num {nums[j]}")
            if ((nums[i] == nums[j]) and (abs(i-j)<=k)):
                found = True
                break
    if found:
        break
            
print(found)
# time limit exceed prob
"""