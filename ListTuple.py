l=[]
a=""
while True:
    a=input("Do you want to enter value")
    if(a=="Y" or a=="Yes" or a=="y" or a=="yes"):
        n=int(input("Enter value"))
        l.append(n)
    if(a=="N" or a=="No" or a=="n" or a=="no"):
        break
print("Values in the form of List=%s" %(l))
t=tuple(l)
print("Values in the form of Tuple=",t)
