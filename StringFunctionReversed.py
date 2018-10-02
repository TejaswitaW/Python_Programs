# Reversing string using reversed function
s=input("Enter any string")
for x in reversed(s):
    print(x,end="")
print()
print("_".join(reversed(s)))
