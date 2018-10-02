#use of instance method and instance variable
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def disp(self):
        print("Dear{x},you got {y} marks".format(x=self.name,y=self.marks))
    def grade(self):
        if self.marks>75:
            print("Dear %s,you got I grade" %(self.name))
        elif self.marks<75:
            print("Dear %s,you got II grade" %(self.name))
        elif self.marks<70:
            print("Dear %s,you got III grade" %(self.name))
        else:
            print("Dear %s,you are Fail" %(self.name))
name=input("Enter name of Student")
marks=int(input("Enter marks of student"))
s=Student(name,marks)
s.disp()
s.grade()
print()
                    
        
