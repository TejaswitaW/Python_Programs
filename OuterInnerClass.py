# Inner and outer class methods
class Outer:
    def m1(self):
        print("Outer class method")
    class Inner:
        def m2(self):
            print("Inner class method")
o=Outer()
j=o.Inner().m2()
i=Outer().Inner()
i=m1()
o.m1()

