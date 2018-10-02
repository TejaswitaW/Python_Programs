# reversing string without using direct function

s=input("Enter a string")

l=len(s)
i=-1
print("Reversed string is:")
while i >=-l:
    print("%s" %(s[i]),end="")
    i=i-1
