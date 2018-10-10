#function inside function
def outer():
    def inner(a,b):
        print("Addition",a+b)
        print("Subtraction",a-b)
        print("Multiplication",a*b)
        print("Division",a/b)
        print("Modulus Division",a%b)
        print("Integer Division",a//b)
    return inner
t=outer()
t(90,10)
