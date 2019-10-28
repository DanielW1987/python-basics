class Car:

    def __init__(self, maker: str, year: int):
        self.maker: str = maker
        self.year: int = year

    class Engine:

        def __init__(self, number: int):
            self.number: int = number

        def start(self):
            print("Engine started")


e = Car.Engine()
e.start()
