#Read multiple values from keyboard in single line
a,b,c,d=[int(x) for x in input("Enter 4 values of number").split("t")]
z=a+b+c+d
print("Z: ",z)
a,b,c,d=[eval(x) for x in input("Enter 4 values of number").split("t")]
print("a is ",a)
print("b is ",b)
print("c is ",c)
print("d is ",d)
