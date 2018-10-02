def outer():
    print("Executing outer function")
    def inner():
        print("Inner function started execution")
        print("Hi i am inner function")
    print("Outer function returning inner funtion see how it is execute")
    return inner()
f1=outer()
print("Now i am calling inner function")
#f1()
