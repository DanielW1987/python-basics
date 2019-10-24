def decor(fun):
    def inner():
        result = fun()
        return result * 2
    return inner


@decor # name of the above function
def num():
    return 5


assert num() == 10


# another example
def how_are_you(fun):
    def inner(n):
        print(fun(n))
        print("How are you?")
    return inner


@how_are_you
def hello(name):
    return "Hello {}".format(name)


hello("Daniel")
