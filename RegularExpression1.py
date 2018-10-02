#Write a regular expression to represent 10 digit mobile number
import re
c=1

while True:
    n=input("Enter mobile number")
    m=re.fullmatch('[6-9][\d]{9}',n)
    
    if (m!=None):
        print(n,"Valid mobile number")
        if c==2:
            break
    else:
        print(n,"Not Valid mobile number")
        if c==2:
            break
    c+=1
       
