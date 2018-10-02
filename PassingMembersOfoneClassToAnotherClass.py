#passing members of one class to another class
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def disp(self):
        print("Employee number is : ",self.eno)
        print("Employee name is : ",self.ename)
        print("Employee salary is : ",self.esal)
class Test:
    def modify(emp):
        emp.esal=emp.esal+1000
        emp.disp()
e=Employee(100,"Tejaswita",70000)
print("Previous salary is: ",e.esal)
Test.modify(e)
