# Base class 1
class Mother:
    def __init__(self,mothername):
        self.mothername = mothername

    def mother(self):
        print(self.mothername)

# Base class 2
class Father:
    def __init__(self,fathername):
        self.fathername = fathername
    def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def __init__(self,mothername,fathername):
        Mother.__init__(self,mothername)
        Father.__init__(self,fathername)


    def parents(self):
        
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

# Driver code
s1 = Son('sita','ram')
s1.parents()