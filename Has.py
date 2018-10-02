import sys
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print("Car is {0},model is {1} and color is {2}".format(self.name,self.model,self.color))
class Employee:
    def __init__(self,ename,eno,ecar):
        self.ename=ename
        self.eno=eno
        self.ecar=ecar
    def empinfo(self):
        print("Name of Employee is %s and Employee number is %d" %(self.ename,self.eno))
        self.ecar.getinfo()
c=Car("Innova","TC5","White")
e=Employee("Tejaswita",101,c)
e.empinfo()
print(sys.getrefcount(c))
print(sys.getrefcount(e))
               
        
