# use of super() method
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatdrink(self):
        print("Biryani Eating and Beer drinking")
class Emp(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def work(self):
        print("Python coding is like drinking chilled beer")
e=Emp("Tejaswita",33,189,70000)
e.eatdrink()
e.work()
