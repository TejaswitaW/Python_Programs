# if you want global variable in function
a=10

def f1():
    a=100
    print(a)
    print(globals()['a'])

f1()
