#logging in python module
import logging  as lg
lg.basicConfig(filename="log1.txt",level=lg.INFO)
# multiple try except block
lg.info("A new request came")
try:
    print("Outer try block")
    try:
        x=int(input("Enter first number"))
        y=int(input("Enter second number"))
        print(x/y)
    except ZeroDivisionError:
        print("Can not divide with zero")
        lg.exception(msg)
    finally:
        print("Inner block finally succsseful")
        lg.exception(msg)
except ValueError:
    print("Please provide int value only")
    lg.exception(msg)
finally:
    print("I am in finally block")
    lg.exception(msg)
lg.exception("Request processing completed")
