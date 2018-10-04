# input is a4k3b2 and output should be aeknbd
s="a4k3b2"
op=""

for x in s:
    if x.isalpha():
        op=op+x
        pre=x
    else:
        newch=chr(ord(pre)+int(x))
        op=op+newch
print(op)
    
        
