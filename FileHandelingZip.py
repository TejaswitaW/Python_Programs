from zipfile import *
f=ZipFile("files.zip","w",ZIP_DEFLATED)
#with what files you are creating zip file
f.write("emp.csv")
f.write("download.jpg")
f.write("t.jpg")
f.write("downloadTsw.jpg")
f.write("abc.txt")
f.write("StarPattern4.py")
print("Zip file created succssefully")
