# String Reversed
s=input("Enter any string")
output=""
n=len(s)-1
while n>=0:
    output=output+s[n]
    n=n-1
print("Reversed string:{0}".format(output))
