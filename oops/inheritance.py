# Method Overloading
class Person(object):
    def __init__(self, gender):
        self.gender = gender
        # print(this.gender)

    def getGender(self):
        print(self.gender)
        print("hi")


class Male(Person):

    def __init(self, male):
        super().__init__(self, male)

    def getGender(self):
        super().getGender()
        print("Male")


class Female(Person):
    def __init(self, female):
        super().__init__(self, female)

    def getGender(self):
        print("Female")


m = Male("Maleparent")
m.getGender()

f = Female("Femaleparent")
f.getGender()
