#pickeling and unpickling of object
import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def disp(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
with open("emp.txt","wb") as f:
    e=Employee(100,"Tejaswita",60000,"Bengluru")
    pickle.dump(e,f)
    print("Pickling of Employee object completed")
with open("emp.txt","rb") as f:
    obj=pickle.load(f)
    print("Employee information after unpickling")
    obj.disp()
    
