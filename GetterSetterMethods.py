class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
n=int(input("Enter number of students"))
for i in range(n):
    s=Student()
    name=input("Enter name of the student")
    s.setName(name)
    marks=int(input("Enter marks of student"))
    s.setMarks(marks)
    print("Hi ",s.getName())
    print("Your marks are: ",s.getMarks())
    print()
