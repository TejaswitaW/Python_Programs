import functools as fs
#use of filter
def iseven(n):
    if n%2==0:
        return True
    else:
        return False

l=list(range(0,100))
l1=list(filter(iseven,l))
print(l1)
l2=list(filter(lambda x:x%2==0,l))
print(l2)
#use of map function
def dub(n):
    return n*2
l=list(range(0,20))
l1=list(map(dub,l))
print(l1)

#use of reduce function
r=fs.reduce(lambda x,y:x+y,l)
print(r)
