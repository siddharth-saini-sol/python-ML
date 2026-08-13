dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
ip = "CMXL"
tup = tuple(ip)
lst = []
for i in tup:
    lst.append(dic.get(i))
print(lst)
total = 0
for i in range(len(lst)-1):
    if lst[i] < lst[i+1]:
        total = total - lst[i]
    else:
        total = total + lst[i]
total = total + lst[-1]
print(total)