#pickeling and unpickling of object
import emp,pickle
f=open("emp.txt","wb") 
n=int(input("Enter number of employees"))
for i in range(n):
    eno=int(input("Enter employee number"))
    ename=input("Enter employee name")
    esal=float(input("Enter employee salary"))
    eaddr=input("Enter employee address")
    e=emp.Employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
f=open("emp.txt","rb")
print("Employee details....")
while True:
    try:
        obj=pickle.load(f)
        obj.disp()
        print()
    except EOFError:
        print("All employess completed")
        break
f.close()
        
