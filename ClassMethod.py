# use of class method
class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{0} walks with {1} legs".format(name,cls.legs))
Animal.walk("Dog")
