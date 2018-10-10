#merging two unsorted list
a=[21,22,23,24,25]
b=[11,12,13,14,15]
i=0
j=0
s=[]
while i<len(a) or j<len(b):
    if a[i]<b[j]:
        s.append(a[i])
        i+=1        
    else:
        print("In B")
        s.append(b[j])
        j+=1
print(s)
