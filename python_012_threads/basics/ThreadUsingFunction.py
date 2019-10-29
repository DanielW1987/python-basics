from threading import Thread
from threading import current_thread


def display_numbers():
    i = 0
    while i <= 100:
        print("{}: {}".format(current_thread().getName(), i))
        i += 1


t1: Thread = Thread(target=display_numbers, name="Thread 1")
t2: Thread = Thread(target=display_numbers, name="Thread 2")

t1.start()
t2.start()
