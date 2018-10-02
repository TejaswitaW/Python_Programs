# Logging in python
import logging as lg

lg.basicConfig(filename="Log2.txt",level=lg.INFO)

lg.info("A new request came")

try:
    x=int(input("Enter first number"))
    y=int(input("Enter second number"))
    print(x/y)
except ZeroDivisionError as msg:
    print("Cannot divide with zero")
    lg.exception(msg)
except ValueError as msg:
    print("Enter only int values")
    lg.exception(msg)

lg.info("Request processing completed")
