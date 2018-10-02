def f1():
    def inner(a,b):
        print("Addition of a and b is: ",a+b)
        print("Average of a and b is: ",a+b/2)
    inner(30,60)
    inner(90,76)
f1()
