# we are going to study static variables
class Student:
    cname="AVOCE"
    cname="PICT"
s1=Student()
print(s1.cname)# PICT
s2=Student()
s2.cname="COEP"
print(s2.cname)#COEP
print("Again we have printed cname using s1 object: ",s1.cname)#PICT
