# Exception handelling
class YoungException(BaseException):
    def __init__(self,arg):
        self.msg=arg
class OldException(BaseException):
    def __init__(self,arg):
        self.msg=arg
age=int(input('Enter age of person'))
if age<18:
    raise YoungException("You are not eligible")
elif age>60:
    raise OldException("You are too old")
else:
    print("Thanks for registration")
