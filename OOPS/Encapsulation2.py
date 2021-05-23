"""privte---private variables cannot be accessed from derived classes
 and outside of base class also"""
class Base:
    def __init__(self):
        print("init of Base class")
        self.__privatevar=500



class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("init of derived class")
        print(self.__privatevar)

d=Derived()#it throws error bcoz it cannot accessed from sub class

b=Base()
print(b.__privatevar)#it throws rror bcoz it cannot be accessed from outside the class as well


