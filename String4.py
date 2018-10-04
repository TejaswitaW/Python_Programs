#remove duplicates present in the string
s="tejaswita"
l=[]
x=""
for i in s:
    if i not in l:
        l.append(i)
        x=x+i #using string concatenation
print(x)
print("".join(l))#using list
t=set(s)
print("".join(t))#using set
