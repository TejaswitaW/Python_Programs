#comparing list objects
x=["Dog","Cat","Mat"]
y=["Dog","Cat","Mat"]
print(x==y)
print("Address of x is : ",id(x))
print("Address of y is : ",id(y))

print("Address of x is : ",id(x[0]))
print("Address of y is : ",id(y[0]))

print(x[0] is y[0])
