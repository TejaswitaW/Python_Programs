#remove instance variable
class Test:
    def __init__(self):
        self.a=20
        self.b=30
        self.c=36
        self.d=40
        self.e=60
        del self.e
t1=Test()
t2=Test()
print("t1:",t1.__dict__)
print("t2:",t2.__dict__)
del t1.d
print("t1:",t1.__dict__)
