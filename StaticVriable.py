#How to access static variable
class Test:
    a=10
    def __init__(self):
        self.b=20
t1=Test()
t2=Test()
t1.b=999
#t1.a=1000
print(t1.a,t1.b)#1000,999
print(t2.a,t2.b)#10,20
Test.a=2000
print(t1.a,t1.b)#2000,999
print(t2.a,t2.b)#2000,20


