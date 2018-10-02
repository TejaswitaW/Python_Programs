# program to display all positions of substring in given main string

s=input("Enter main string")
subs=input("Enter substring")
n=len(s)
flag=False
pos=-1

while True:
    pos=s.find(subs,pos+1,n)
    if pos==-1:
        break
    print("Your substring found at %i" %(pos))
    flag=True
if flag==False:
    print("Your substring not found")
