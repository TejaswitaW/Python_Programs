import sys
class X:
    a=10
    def m1(self):
        print("Parent reference method")
    @classmethod
    def m2(cls):
        print("This is parent class method")
    @staticmethod
    def m3():
        print("This is parent class static method")
    def __init__(self):
        print("This is parent class constructor")
    def __del__(self):
        print("Parent destructor")
class Y(X):
    a=9999
y=Y()
print(y.a)
y.m1()
y.m2()
y.m3()
print(sys.getrefcount(y))
