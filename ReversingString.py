#reversing string using inbuilt function and without inbuilt function
s="My name is Tejaswita"

#String reversal using inbuit function
for i in reversed(s):
    print(i,end="")
print()

#String reversal using without inbuit function
print(s[::-1])

#string reversal different method
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
print()

#string reversal using another method
i=len(s)-1
while i>=0:
    print(s[i],end="")
    i-=1
