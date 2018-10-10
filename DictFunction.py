#entering name and percentage of student using dictionary
rec={}
n=int(input("Enter number of students"))
i=0
while i<=n:
    name=input("Enter name of student")
    marks=float(input("Enter marks of student"))
    rec[name]=marks
    i+=1
for x in rec:
    print(" ",x," ",rec[x])
