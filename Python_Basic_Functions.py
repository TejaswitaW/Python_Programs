#all basic functions of python in one file
#implementation of ternery operator in python
a=90
x=10
x=30 if a>20 else 40
print(x)
#nesting of conditional operator
x=10 if 20>30 else 50 if 30>40 else 70
print(x)
#finding maximum value using conditional operators
a,b,c=100,200,300
max=a if a>b and a>c else b if b>c else c
print(max)
#identity operator for reference comparision
d=100
print(a is d)
print(d is c)
print(d is not b)
#use of membership operator
l=[23,12,90,"Python","Python","n"]
print(100 in l)
print("Python" in l)
print("Program" not in l)
print("n" in l)
s="Python"
print(("z" or "n") in s)
print("n" and "z")
