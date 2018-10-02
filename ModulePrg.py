
import time
from imp import reload
import module1
print("We are accesing module 1 in this program")
time.sleep(30)
reload(module1)
print("This is last line of program")
