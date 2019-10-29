from threading import *


class MyThread:

    def display_numbers(self):
        i = 0
        while i <= 100:
            print("{}: {}".format(current_thread().getName(), i))
            i += 1


my_thread: MyThread = MyThread()
t1: Thread = Thread(target=my_thread.display_numbers, name="Thread 1")
t2: Thread = Thread(target=my_thread.display_numbers, name="Thread 2")

t1.start()
t2.start()
