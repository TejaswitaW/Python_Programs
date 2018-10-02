# multiple error handeling by single except block
try:
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    print(a/b)
except(ZeroDivisionError,ArithmeticError,ValueError)as msg:
    print("Please enter proper data values")
