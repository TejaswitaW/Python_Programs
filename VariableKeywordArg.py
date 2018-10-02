# variable length keyword arguments
def display(**kwargs):
    print(type(kwargs))
    print("Record Information")
    for k,v in kwargs.items():
        print(k,"     ",v)

        
