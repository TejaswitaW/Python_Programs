# string reverse using list

s=input("Enter some string")
l1=s.split()
print(l1)
n=len(l1)-1

l=[]

while n>=0:
    l.append(l1[n])
    n=n-1
    
print(l)
output=" ".join(l)
print(output)
