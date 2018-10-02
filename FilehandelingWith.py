# File handeling with "with" keyword
with open("test1.py","w")as f:
    f.write("""print("Hello World")""")
    f.write("""print("Hello Tejaswita")""")
    print("Is file closed: ",f.closed)
print("Is file closed: ",f.closed)
