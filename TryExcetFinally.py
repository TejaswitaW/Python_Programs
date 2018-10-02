# try with multiple except and finally block
try:
    x=int(input("Enter first number"))
    y=int(input("Enter second number"))
    print(x/y)
except ZeroDivisionError:
    print("Can not divide with zero")
except ValueError:
    print("Please provide int value only")
finally:
    print("I am in finally block")
    
