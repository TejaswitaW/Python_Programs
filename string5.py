#Find number of occurrences of each character in string
s="ABCABCABABAB"
d={}
# uses character as key
#number of occurences as values
for x in s:
    if x not in d.keys():
        d[x]=1 
    else:
        d[x]=d[x]+1
for k,v in d.items():
    print("{} occurs {} times".format(k,v))
