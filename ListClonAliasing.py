#aliasing and clonning in list
print("List aliasing is done here")
x=[10,20,30,40]
y=x
print("Address of x after aliasing",id(x))
print("Address of y after aliasing",id(y))
print(x)
print(y)
#above code is for aliasing
print("List clonning using copy method")
y=x.copy()
print("Address of x after copy method",id(x))
print("Address of y after copy method",id(y))
print(x)
print(y)
#clonning is done using copy method
print("List clonning is done using slicing operator")
y=x[:]
print("Address of x after slicing method",id(x))
print("Address of y after slicing method",id(y))
print(x)
print(y)
#clonning is done using slicing method
