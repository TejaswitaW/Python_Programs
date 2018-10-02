#program to find file exist or not
import os,sys
fname=input("Enter file name")
if os.path.isfile(fname):
    print("file exist:",fname)
    f=open(fname,'r')
    data=f.read()
    print(data)
else:
    print("File not exist",fname)
    sys.exit(0)
