#protected---protected memebers can be accessed from within the drived classes but not from outside class
class Base:
    def __init__(self):
        print("init of  class")
        self._protectedvar=1000




class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("init of derived class")
        print(self._protectedvar)

d=Derived()#since is accessed from sub class,value will be printed
#
# b=Base()
# print(b.protectedvar)//this line gives error as it is accessed from outside the class


