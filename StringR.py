# finding substring in given string
s="durgasoftdurgasofthydrabaaddurgasoftsoftsoft"
sb="soft"
i=0
j=0
st=""
print(id(st))
while i<len(s):
    if sb[j]!=s[i]:
        st=st+s[i]
        i+=1
        continue
    elif sb[j]==s[i]:
        print(sb[j],end="")
        j+=1
        i+=1
        if j>=len(sb):
            print(" At Index: ",i-j)
            st=st+"good"
            j=0
            continue
print(st)
print(id(st))
