from threading import *
import time
def wish(name):
    for i in range(10):
        print("Good Evening:",name)
        time.sleep(1)
    time.sleep(2)

t1=Thread(target=wish,args=('Seetha',))
t2=Thread(target=wish,args=('Rama',))
t1.start()
t1.join()
t2.start()
