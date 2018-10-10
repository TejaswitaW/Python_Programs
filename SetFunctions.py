#functions related to set
s=set(range(0,6))
print(s)
s.add(90)
print(s)
l=[10,20,30,40,50]
s.update(l)
print(s)
s.update("kh"+"df")
print(s)
s1=s
print(s1)
print(s.pop())
print(s)
print(s1)
s.remove(50)
print(s)
print(s1)
print(s1.intersection(s))
print(s1.union(s))
print(s1.symmetric_difference(s))
t=set("Tejaswita")
print("t" in t)
x={0,1,2,3,4,5,6}
y={i*i*i for i in x}
print(y)
z={i for i in x if i%2==0}
print(z)
