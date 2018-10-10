#word frequency counter using dictionary
s="My name is Tejaswita Sitaram Wakhure name name NAME NAme"

t=s.split()

print(t)
#simple Method
print(len(t))
#using dictionary
d={}.fromkeys(t,0)
#print(d[0])
for i in t:
    
    d[i]+=1
    
print("Words in string: ",d)
    
