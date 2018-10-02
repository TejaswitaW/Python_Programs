#use of destructor
import sys
import time
class Test:
    def __init__(self):
        print("Constructor execution")
    def __del__(self):
        print("Destructor Execution")
t1=Test()
t2=t1
t3=t2
print(sys.getrefcount(t1))
tz=Test()
tx=[Test(),Test(),Test()]
del t2
print(sys.getrefcount(t1))
time.sleep(5)
print("Object not yet destroyed after deleting t1")
#del t2
time.sleep(5)
print("Object not yet destroyed after deleting t2")
#del t3
#del tz
#del tx
print("End")
        
