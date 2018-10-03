#String functions
s=input("Enter any string")

if s.isalnum():
    print("Alphnumeric string")
    if s.isalpha():
        print("Alphabetical string")
        if s.islower():
             print("Lowercase string")
        else:
             print("Uppercase string")
    else:
        print("Numeric string")
elif s.isspace():
    print("It is space character")
else:
    print("Non space special character")
