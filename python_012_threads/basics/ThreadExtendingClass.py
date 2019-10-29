from threading import Thread
from threading import current_thread


class MyThread(Thread):

    def __init__(self, name: str):
        super().__init__()
        self.setName(name)

    def run(self) -> None:
        self.display_numbers()

    def display_numbers(self):
        i = 0
        while i <= 100:
            print("{}: {}".format(current_thread().getName(), i))
            i += 1


t1: Thread = MyThread("Thread 1")
t2: Thread = MyThread("Thread 2")

t1.start()
t2.start()
