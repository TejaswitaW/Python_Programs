#use of destructor
import time
class Test:
    def __init__(self):
        print("Object Initialisation")
    def __del__(self):
        print("Fulfilling last wish and performing clean up activity")
t1=Test()

del t1
time.sleep(5)
print("End of application")
