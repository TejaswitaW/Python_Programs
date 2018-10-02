# use of reduce function
import functools as fn
l=[10,20,30,40,50,60,70,80,90,100]
l1=fn.reduce(lambda x,y:x+y,l)
print(l1)
