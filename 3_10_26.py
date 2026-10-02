nums = [1,1,1,2,2,3,3,4,5,6,7,7,8]
"""
n = len(nums)
j = 0 
ik = 0
freq = {}
for i in range(0,n):
    freq[nums[i]] = freq.get(nums[i],0)+0
for k in freq:
    nums[j] = k
    j=j+1
print(j)
print(nums)

n = len(nums)
dic = {}
count = 0
for i in range(0,n):
    if nums[i] not in dic:
        dic[nums[i]] = 0
        
    else:
        continue
for i in dic:
    nums[count] =  i
    count = count+1
print(count)
print(nums)
"""

n = len(nums)
i= 0
j = i+1
while(j<n):
    if nums[i]!=nums[j]:
        i=i+1
        nums[i],nums[j]=nums[j],nums[i]
    j=j+1
print(i+1)
print(nums)