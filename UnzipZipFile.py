# working with zip file(unzipping zip file)
from zipfile import *
f=ZipFile("files.zip",'r',ZIP_STORED)
names=f.namelist()
for name in names:
    print("Name of the file is: ",name)
    print("The content of the file is:")
    f1=open(name,"r")
    print(f1.read())
    print()
    
    
