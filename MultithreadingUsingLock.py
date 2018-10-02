#multithreading using semaphore
from threading import *
import time
s=BoundedSemaphore()
def wish(name):
    s.acquire()
    for i in range(5):
        print("Good evening:",end='')
        time.sleep(5)
        print(name)
    s.release()
#   s.release()
t1=Thread(target=wish,args=("Tejaswita",))
t2=Thread(target=wish,args=("Titu",))
t3=Thread(target=wish,args=("Sweety",))
t1 .start()
t2.start()
t3.start()
