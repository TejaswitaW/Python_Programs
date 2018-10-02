# to check the content of string

s= input("Enter some string")
if s.isalnum():
    print("Alphnumeric character")
    if s.isalpha():
        print("Alphabetical String")
        if s.lower():
            print("Lowercase alphabet character")
        else:
            print("Uppercase alphabet character")
    else:
        print("It is digit string")
elif s.isspace():
    print("It is space character")
else:
    print("It is special character string")
