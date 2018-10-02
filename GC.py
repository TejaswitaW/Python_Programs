import time
class Test:
    def __del__(self):
        print("Destructor execution")
t1=Test()
t2=Test()
t3=Test()
t4=Test()
t5=Test()
t6=Test()
t7=Test()
time.sleep(10)
