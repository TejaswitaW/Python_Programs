#use of class inside class
class Person:
    def __init__(self):
        self.name='Durga'
        self.db=self.Dob()
    def disp(self):
            print("Name is %s " %(self.name))
    class Dob:
        def __init__(self):
             self.dd=28
             self.mm=5
             self.yy=1984
        def disp(self):
             print("Dob is {0}/{1}/{2}".format(self.dd,self.mm,self.yy))
p=Person()
p.disp()
p.db.disp()
