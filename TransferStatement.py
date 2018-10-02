# use of for ,if,else, break
cart=[100,200,300,400,500,600,700]

for item in cart:
    if item>400:
        print("Sorry we can not process your request")
        print("I am exiting from the process")
        break
    print("Processing your item: ",item)
else:
    print("Your all items are processed")
