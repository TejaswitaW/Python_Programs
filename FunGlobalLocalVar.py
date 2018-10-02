#Program for use of local and global variables
a=10
def f1():
    global a
    a=777
    print("f1",a)
def f2():
 #   global a
 #   a=777
    print("f2",a)
f1()
f2()
f2()
f1()
