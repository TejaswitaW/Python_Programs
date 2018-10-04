#input is s1=RAVI,S2=TEJA output is RTAEVJIA
s1="RAVI"
s2="TEJA"
op=""
i=0
j=0

while i<len(s1) or j<len(s2):
    op=op+s1[i]+s2[j]
    i+=1
    j+=1
    
print(op)
    
