# use of reduce function
import functools as fn
sum=0

def addition(x):
    for i in x:
        sum=sum+i
    return sum

l=list(range(1,10000))
l2=fn.reduce(addition,l)
print(l2)
