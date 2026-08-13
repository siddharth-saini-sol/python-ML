def func():
    n = 687
    num = n 
    while(num >0):
        last_digit= num%10
        print(last_digit)
        num = num//10


def func2():
    n = 456
    num = n
    count = 0
    while(num>0):
       #dig = num%10
       num = num//10
       count = count+1
       print(count)

def func3():
    n = 1213
    num = n
    res = 0
    while (num>0):
        last_dig = num%10
        res = (res*10)+last_dig
        num = num//10
    print(res)
    if res == n:
        print('paladrom no')
    else:
        print('no it not')
    


func()
func2()
func3()
