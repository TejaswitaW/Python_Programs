#program to display unique vowels present in the word
s="My name is Tejaswita Sitaram Wakhure I am working in bengluru"
v=["A","a","i","I","o","O","U","u"]
f=[]
for i in s:
    if i in v:
        if i not in f:
            f.append(i)
print(f)
        
