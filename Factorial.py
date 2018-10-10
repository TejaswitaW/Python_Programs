#function to write facorial of given number
n=4
def fact(n=8):
    f=1
    while n>=1:
        f=f*n
        n-=1
    return f
f=fact()
print(f)
