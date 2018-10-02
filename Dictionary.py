# first dictionary program
rec={}
n=int(input("Enter number of students"))
i=1
while i<=n:
    name=input("Enter name of the student")
    marks=float(input("Enter marks of the student"))
    rec[name]=marks
    i=i+1

#print(rec)
print("Name of student","% of marks")
for x in rec:
    print("\t",x,"\t",rec[x])
    


    
