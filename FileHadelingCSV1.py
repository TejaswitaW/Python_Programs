#reading data from csv file
import csv
f=open("emp.csv","r")
r=csv.reader(f)# returns reader object
data=list(r)
print(data)
print(type(data))
for i in data:
    for word in i:
        print(word,"\t",end="")
    print()
