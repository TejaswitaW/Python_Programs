# playing with binary files
f1=open("download.jpg","rb")
f2=open("t.jpg","wb")
bytes=f1.read()
f2.write(bytes)
print("New image is available with t.jpg")
