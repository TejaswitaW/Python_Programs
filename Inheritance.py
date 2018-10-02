#inheritance
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print("Here2")
        print("Car name {0},Car model {1},Car color {2}".format(self.name,self.model,self.color))
class Employee:
    def __init__(self,eno,ename,ecar):
        self.ename=ename
        self.eno=eno
        self.ecar=ecar        
    def empinfo(self):
        print("Employee name: ",self.ename)
        print("Employee number: ",self.eno)
        print("Employee car info")
        self.ecar.getinfo()
c=Car('Innova','2.5Z','Grey')
e=Employee(100,'Durga',c)
        
