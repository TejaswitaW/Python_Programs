#use of filter function
def iseven(x):
    if x%2==0:
        return True
    else:
        return False
l=list(range(1,100))
l1=list(filter(iseven,l))
print(l1)

