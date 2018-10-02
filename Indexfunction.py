# use of index with exception handelling

s=input("Enter a string")
subs=input("Enter a substring")
flag=1

try:
    s.index(subs)
except ValueError:
          flag=0
          print("Your substring could not find")
finally:
          print("Your request is processed")
          if flag==1:
              print("Your substring found")
    
