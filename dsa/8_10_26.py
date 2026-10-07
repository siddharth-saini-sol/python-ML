arr2 = [1,2,3,4,5,6,7]
arr= [0,1,2,3,4,5]
k = 9
if k > len(arr):
    k = k%len(arr)  #9 % 6 = 3
end = len(arr)-k
for i in range(0,k):
    for j in range(len(arr)-1,end-1,-1):
        arr[i],arr[j]=arr[j],arr[i]
print(arr)
print(4%3)

nums = [0,1,2,3,4,5]
k = 1
n = len(nums)
k = k%n
nums[:] = nums[n-k:]+nums[:n-k] #nums[6-1 =5:]+nums[:5]
print(nums)
