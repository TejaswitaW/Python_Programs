# simple file handeling

f=open("test.txt","r")
print(f.tell())
f.write("Durga")
data=f.read(4)
print(data)
print(f.tell())
f.close()
