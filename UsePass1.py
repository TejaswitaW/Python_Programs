#Use of Pass statement
n=0

for i in range(100):
    if i%2==0:
        pass
    else:
        print("hi",i)
        n=n+1
print("Total numbers= ",n)
