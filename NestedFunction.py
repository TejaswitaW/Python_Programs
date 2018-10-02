# nested function concept
def outer():
    print("outer function1")
    def inner():
        print("Inner function")
        return ininner()
    def ininner():
        print("I am inside inner function")
    return inner()
outer()
