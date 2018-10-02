# try with multiple except and finally block with os module
import os
import sys
try:
    x=int(input("Enter first number"))
    y=int(input("Enter second number"))
    print(x/y)
    os._exit(0)
except ZeroDivisionError:
    print("Can not divide with zero")
except ValueError:
    print("Please provide int value only")
finally:
    print("I am in finally block")
