from threading import *
import time
##print("Current thread is1:",current_thread().getName())
##def disp():
##    for i in range(1,11):
##        print("Child Thread")
##   
##
##Thread(target=disp).start()
##time.sleep(5)
##for i in range(1,11):
##    print("Main Thread")
##class MyThread(Thread):
##    def run(self):
##        for i in range(10):
##            print("Child Thread 1")
##t=MyThread()
##t.start()
print("Current thread name is: ",current_thread().getName())
current_thread().setName("Tejaswita")
print("Current thread number is: ",current_thread().ident)
def doubles(numbers):
    current_thread().setName("hi doubles")
    for i in numbers:
        time.sleep(1)
        print("Doubles:",i*2)
    print("Current thread name is: ",current_thread().getName())
    print("Current thread number is: ",current_thread().ident)
def squares(numbers):
    current_thread().setName("hi squares")
    for i in numbers:
        time.sleep(1)
        print("Squares:",i**2)
    print("Current thread name is: ",current_thread().getName())
    print("Current thread number is: ",current_thread().ident)
numbers=[1,2,3,4,5]
b=time.time()
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
time.sleep(5)
t2.start()
t1.join()
t2.join()
e=time.time()
print("Total time required for execution is:",e-b)
print("Current thread number is: ",current_thread().ident)
print("Current thread name is: ",current_thread().getName())
print("Number of active threads:",active_count())
l=enumerate()
print(l)
