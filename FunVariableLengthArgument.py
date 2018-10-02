#Function uses variable number of arguments

def sum(*n):
    sum=0
    for x in n:
        sum=sum+x
    print("The result of sum=%d" %sum)
    

