#use of function decorator
def d(func):
    def smartdivision(a,b):
        if b==0:
            print("You can not divide by zero,be careful")
        else:
            func(a,b)
    return smartdivision


def div(a,b):
    print(" ",a/b)
    
decor=d(div)

decor(9,1)
decor(9,2)
decor(9,0)
