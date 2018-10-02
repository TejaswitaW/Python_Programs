from threading import *
import time

def disp():
    
    for i in range(10):
        print("Seetha thread")
        time.sleep(2)
t=Thread(target=disp)
t.start()
t.join()
print(t.isDaemon())
for i in range(10):
    print("Rama thread")
