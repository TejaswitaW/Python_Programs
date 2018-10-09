#list comprehension
x=[1,2,3,4,5,6,7,8,9,10]
l=[i*i for i in range(len(x))]
l2=[i*i for i in x]
print(l)
print(l2)
