'''
class students:
    name = 'Ali'
    rollNo=1
    def input(self):
        self.name=input("Enter your name=")
        self.rollNo=int(input("Enter your roll number="))
    def print(self):
        print(f"Name: {self.name}\nRoll No:{self.rollNo}")
first=students()
first.input()
first.print()
'''
'''
class students:
    name = 'Ali'
    rollNo=1
    Grade="B+"
    age=17
    def method(self):
        print(self.name)
        print(self.rollNo)
        print(self.Grade)
        print(self.age)
first=students()
second=students()
first.method()
first.name
second.rollNo=16    
'''
class Gfather:
    D_O_E=None
    car=""
    def __init__ (self, D_O_E , car):
        self.D_O_E=D_O_E
        self.car=car
obj1=Gfather(1989,"City")
print("-----------")
print(obj1.D_O_E)
print(obj1.car)

class father(Gfather):
    Job=""
    scale=None
    def __init__ (self,D_O_E,car,job , scale):
        super().__init__(D_O_E,car)
        self.job=job
        self.scale=scale
obj2=father(1990,"Civic","Cleark",15)
print("-----------")
print(obj2.D_O_E)
print(obj2.car)
print(obj2.job)
print(obj2.scale)

class son(father):
    Name=""
    age=None
    def __init__(self,D_O_E,car,job,scale,Name,age):
        super().__init__(D_O_E,car,job,scale)
        self.Name=Name
        self.age=age
obj3=son(2002,"Thar","DPO",17,"Rao Hassan",18)
print("-----------")
print(obj3.D_O_E)
print(obj3.car)
print(obj3.job)
print(obj3.scale)
print(obj3.Name)
print(obj3.age)
