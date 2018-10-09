#Take tuple form keyboard and return its sum and average
t=eval(input("Enter tuple of numbers in comma seperated value"))
a=0
print(t)
for i in range(0,len(t)):
    a+=t[i]
print("Sum of all numbers in tuple is: ",a)
ag=a/len(t)
print("Average of numbers is ",ag)
