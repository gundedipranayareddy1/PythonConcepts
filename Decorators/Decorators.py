def decoratetest(func):
    def inner():
        print("hey,i am decorated method")
        func()
    return inner


@decoratetest
def test():
    print("i am test method")

test()

#*args,**kwargs

def checkifeven(func):
    def inner(args):
        print("checking!")
        if args%2==0:
            print("even")
            func(args)
        else:
            print("odd")
            func(args)
    return inner

@checkifeven
def evenorodd(num):
    print("i {} am tested finally for even or odd".format(num))

evenorodd(3)


#**kwargs

def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))
    print(data["Firstname"])

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

