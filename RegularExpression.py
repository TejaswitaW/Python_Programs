#regular expression
import re
##s=re.subn('\d','#','a7b9c1d4')
##print("String after replacement:",s[0])
##print("Number of replacement: ",s[1])
##l=re.split('_','10_20_30_40_50')
##print(l)
##l=re.split("[.]","www.tejaswitawakhure.com")
##for i in l:
##    print(i)
##s="Learning is very easy"
##res=re.search("^Learn",s)
##if res!=None:
##    print("Yes")
##else:
##    print("No")
s=input("Enter identifier to validate")
t=re.fullmatch('[a-k][0369][a-zA-Z0-9#]',s)
if t!=None:
    print("Valid Identifier")
else:
    print("Invalid Identifier")
