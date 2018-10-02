#program to generate random password of length 6
#1,3,5 are alphabetic symbol
#2,4,6 are digit
from random import *

for i in range (10):
    print(chr(randint(65,90)),randint(0,9),chr(randint(65,90)),randint(0,9),chr(randint(65,90)),randint(0,9),sep="")
