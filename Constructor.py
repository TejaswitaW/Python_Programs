# Learning constructor
class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
s1=Student("Durga",101,98)
print(s1.name,s1.rollno,s1.marks)
s2=Student("Maya",102,95)
print(s2.name,s2.rollno,s2.marks)
print(s1)
