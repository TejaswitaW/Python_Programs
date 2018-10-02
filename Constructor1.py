#constructor with multiple optional arguments
class Student:
    def __init__(self,n,m):
        self.name=n
        self.marks=m
    def display(self):
        print("Hi",self.name)
        print("Marks",self.marks)
s1=Student()
s1.display()
s2=Student("Rama",100)
s2.display()
    
