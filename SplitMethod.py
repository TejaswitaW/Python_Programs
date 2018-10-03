#string reversal using split method
s="My name is Tejaswita"
l=s.split()
print(l)
for i in range(len(l)-1,-1,-1):
    print(l[i],end=" ")
print()

#string reversal of words in string    
for i in range(len(l)-1,-1,-1):
    for j in reversed(l[i]):
        print(j,end="")
    print(end=" ")    
