count = 1
def func(n):
    global count
    if(n==1 or n==0):
        return 1
    count = count * n
    func(n-1)
func(19)
print(count)

num = [1,2,3,4,5,6,7,8,9] #[1,2,6,5,4,3,7,8,9]
left = 2
right = 5
def func(left , right):
    global num 
    if left >= right  :
        return 
    num[left],num[right] = num[right],num[left]
    print(f"left = {left}")
    print(f"right = {right}")
    print(num)
    func(left +1,right-1)
func(left , right)


    

    

