#inter threading communication
from threading import *
import time
e=Event()
def con():
    print("Consumer is waiting for signal")
    e.wait()
    print("Consumer thread got notification and consuming items")
def prod():
    time.sleep(10)
    print("Producer is producing items")
    print("Prducer thread giving notification by setting event")
    e.set()

t1=Thread(target=prod)
t2=Thread(target=con)
t1.start()
t2.start()
