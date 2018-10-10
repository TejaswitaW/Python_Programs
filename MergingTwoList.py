#Merging two sorted list
a=[1,2,3,4,5]
print(a)
b=[11,12,13,14]
print(b)
#merging using list concatenation
print(sorted(a+b))
#merging using list extend function
##a.extend(b)
##print(sorted(a))
#merging using while loop
s=[]
while a and b:
    if a[0]<b[0]:
        s.append(a.pop(0))
    else:
        s.append(b.pop(0))
print(s+a+b)
        

