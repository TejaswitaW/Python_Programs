# map function
def double(x):
    return 2*x
l=[3,4,5,6]
l1=tuple(map(double,l))
print(l1)
print(type(l1))
