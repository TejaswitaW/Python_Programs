import sys
class Customer:
    '''Customer class with bank operation'''
    bankname="ICICI"
    def __init__(self,name,bal=0):
        self.name=name
        self.bal=bal
    def deposit(self,amt):
        self.bal=self.bal+amt
        print("Updated balance in your account is: ",self.bal)
    def withdraw(self,amt):
        if self.bal<amt:
            print("Insufficient funds")
            sys.exit()
        else:
            self.bal=self.bal-amt
            print("Updated balance in your account is: ",self.bal)
print('Welcome to ',Customer.bankname)
name=input("Enter your name:")
c=Customer(name)
#c.name=name
while True:
    print('d-Deposit\nw-Withdraw\ne-exit')
    option=input('Choose your option')
    if option=='d' or option=='D':
        amt=float(input("Enter amount"))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input("Enter amount"))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("Thanks for banking with us")
        sys.exit()
    else:
        print("Invalid Option")
    
    
        
