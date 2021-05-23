from abc import ABC,abstractmethod,abstractproperty

class Parent(ABC):
    @abstractmethod
    def quality(self):
        pass
    def basic(self):
        print("i am a concrete method")



class Child(Parent):
    def quality(self):
        print("child quality")
#p=Parent() #executing this line will throwyou an eror bcoz we cannot instantiate an abstract class

c=Child()
c.quality()
c.basic()


