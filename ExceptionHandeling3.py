# multiple try except block
try:
    print("Outer try block")
    try:
        x=int(input("Enter first number"))
        y=int(input("Enter second number"))
        print(x/y)
    except ZeroDivisionError:
        print("Can not divide with zero")
    finally:
        print("Inner block finally succsseful")
except ValueError:
    print("Please provide int value only")
finally:
    print("I am in finally block")
