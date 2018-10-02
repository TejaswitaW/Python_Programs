# print extension of a file
fp=input("Enter filename")
i=0
n=len(fp)
while i<n:
    if fp[i]==".":
        print(fp[i+1:n])
        break
    i=i+1
l=fp.split(".")
print(l[1])
    
