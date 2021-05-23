# Method overriding
class Parent(object):
    def __init__(self):
        print("i m parent")

    def show(self):
        print("show of parent")

    def display(self):
        print("display of parent")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("i am child")

    def show(self):
        print("Calling show method of parent using 'Parent.show()'")
        Parent.show(self)
        print("show of child")

    def display(self):
        print("Calling display method of parent using super.display()")
        super().display()
        print("display of child")


c = Child()
p = Parent()
p.show()
c.show()
p.display()
c.display()
