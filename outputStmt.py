#Basic Functionalities in python
#use of seperator
a,b,c=10,20,30
print(a,b,c,sep=":")
print("Values of a,b and c ",a,b,c,sep="*")
#use of end
a,b,c=10,20,30
print(a,b,c,sep=":")
print("Values of a,b and c ",a,b,c,end="\n")
print("Hellooo World","Hi How are you",end=" ")
print("Namste")
name="Tejaswita"
salary=70000
company="JP Morgan Chase"
print("Name of Employee is {}.\
Organization name is {}. Salary is {}".format(name,company,salary))
print("Name of Employee is {2}.\
Organization name is {1}. Salary is {0}".format(salary,company,name))
name="TejaswitaW"
salary=7000000
company="JP Morgan Chase USA"
print("Name of Employee is %s.\
Organization name is %s. Salary is %i" %(name,company,salary))
