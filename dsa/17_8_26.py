count = 0
def func(x,y):
    global count
    if(count==y):
        return 
    count = count+1
    func(x,y)
    print(x)
func(3,3)