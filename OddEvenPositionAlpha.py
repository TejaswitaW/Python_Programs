#seperating odd and even spaced alphabets
s="My name is Tejaswita"

print("Alphabets at even position")
for i in range(0,len(s),2):
    print(s[i],end="")

print()

print("Alphabets at odd position")
for i in range(1,len(s),2):
    print(s[i],end="")

print()
