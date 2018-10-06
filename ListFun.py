#List related functions
l=list(range(0,15))#list created using range
print(l)
for x in l:
    print(x,end=" ")#accessing list element using for loop
print()
#length of string
print(len(l))
#number of occurences of each object
print(l.count(10))
#index of a object
print(l.index(10))#if element is not in the list it gives error
#print(l.index(100))
#finding the object is present or not in the list
t=int(input("Enter target to be found"))
if t in l:
    print("Given target is in list",(l.index(t)))
else:
    print("Target not found in list at index ")
nl=[]
#appending elements in the list
nl.append(100)
nl.append(200)
nl.append(300)
nl.append(400)
nl.append(500)
print(nl)
a=[]
v=1000
for i in range(0,11):
    a.append(v)
    v+=100
print(a)
#use of insert function
a.insert(100,19)
print(a)
a.insert(-100,19)
print(a)
#use of extend function
a.extend(l)
print(a)
a.extend((1,2,3,4))
print(a)
