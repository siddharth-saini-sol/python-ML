dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
ip = "CMXL"
lst = list(ip)
print(lst)
lst = [dic.get(item) for item in lst]
print(lst)
print(dic.get('C'))
print(dic.get("M"))