# File handeling concept in detail
with open("StringReverse5.py","r")as t:
    data=t.read()
    print(data)
    print("In this we have written code to the screen Using Program")
    print(t.tell())
    t.seek(7)
    print(t.tell())
#print("In this we have written code to the screen Using Program")
