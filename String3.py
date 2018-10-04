#input is s1=RAVI,S2=TEJA output is RTAEVJIA
s1="RAVI"
s2="TEJA"
op=""
i=0
j=0

while i<len(s1) or j<len(s2):
    if i<len(s1):
        op=op+s1[i]
        i+=1
    if j<len(s2):
        op=op+s2[j]
        j+=1
        
print(op)
    
