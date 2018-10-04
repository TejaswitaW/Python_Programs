#seperate alphabets and string in digits
s="123tejaswitahapp198ygirl$%&*"
i=0
sdigit=""
salpha=""

while i<len(s):
    if(str(s[i])>='0' and str(s[i])<='9'):
       sdigit=sdigit+s[i]
       i+=1
    elif (str(s[i])>='a' or str(s[i])<='z') and (str(s[i]) >='A' or str(s[i])<='Z'):
        salpha=salpha+s[i]
        i+=1
           
print(sdigit)
print(salpha)

print(sdigit+salpha)
