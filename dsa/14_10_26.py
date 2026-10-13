nums = [1,0,2,4,3,0,0,3,5,1]
for i in range(0,len(nums)):
    for j in range(i,len(nums)-1):
        if nums[i] ==0 and nums[j]==0:
            j=j+1
        if nums[i] ==0:
            nums[i],nums[j]=nums[j],nums[i]
print(nums)


nums = [0,1,0]
for i in range(0, len(nums)-1):
    pt = 0
    if nums[i] ==0:
        pt = nums[i]
        nums.remove(nums[i])
        nums.append(pt)
print(nums)


nums = [1,0,2,4,3,0,0,3,5,1]
lst_zeros = []
lst_nums = []
for i in range(0, len(nums)):
    if nums[i] == 0 :
        lst_zeros.append(nums[i])
    else:
        lst_nums.append(nums[i])
nums[:] = lst_nums+lst_zeros
print(nums)


