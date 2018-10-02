#File handeling
f=open("abc.txt",'r+')
f.write("Hi Hello How are you dear Tejaswita,My love")
f.writelines("Hello Dear\n My name is Python\nI am very easy to learn\nYou can do any programming in me\n you can easily learn me ok.........")
data=f.read(11)
print(data)
print(f.tell())
print(f.name)
print(f.mode)
print(f.closed)
if f.readable()==True:
    print("Readable")
else:
    print("Writable")
f.close()
print(f.closed)
