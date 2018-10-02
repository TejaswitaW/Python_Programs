#program to display all positions of substring in string
s=input("Enter any string")
subs=input("Enter substring")
pos=-1
flag=False
while True:
    pos=s.find(subs,pos+1,)
    if pos==-1:
        break
    else:
        print("Index of string is : ",pos)
        flag=True
if(flag==False):
    print("String Not Found")
