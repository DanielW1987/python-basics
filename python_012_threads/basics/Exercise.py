import threading
from threading import Thread


class EvenNumbersThread(Thread):

    def __init__(self, name: str):
        super().__init__()
        self.setName(name)

    def run(self) -> None:
        for i in range(0, 101, 2):
            print(threading.current_thread().getName(), ":", i)


class OddNumbersThread(Thread):

    def __init__(self, name: str):
        super().__init__()
        self.setName(name)

    def run(self) -> None:
        for i in range(1, 101, 2):
            print(threading.current_thread().getName(), ":", i)


t1: Thread = EvenNumbersThread("Even number")
t2: Thread = OddNumbersThread("Odd number")

t1.start()
t2.start()
