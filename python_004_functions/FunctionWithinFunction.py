def display(name: str):
    def greeting():
        return "Hello "

    return greeting() + name


message: str = display("World")
print(message)
