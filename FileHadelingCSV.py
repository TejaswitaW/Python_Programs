#writing data to csv file
import csv

with open("emp.csv","w",newline="") as f:
    w=csv.writer(f) # returns csv writer object pointing to f
    w.writerow(["ENO","ENAME","ESAL","EADDR"])
    n=int(input("Enter number of employees"))
    for i in range(n):
        eno=int(input("Enter employee number"))
        ename=input("Enter name of employee")
        esal=float(input("Enter employee salary"))
        eaddr=input("Enter employee address")
        w.writerow([eno,ename,esal,eaddr])
print("Data is succssefully inserted to csv file")
