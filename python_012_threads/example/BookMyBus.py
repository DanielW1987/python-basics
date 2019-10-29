from threading import *
from time import sleep


class BookMyBus:

    def __init__(self, available_seats: int):
        self.__available_seats = available_seats
        self.__lock = Lock()

    def buy(self, seats_requested: int):
        # self.__lock.acquire()
        sleep(3)
        print("Total seats available:", self.__available_seats)

        if self.__available_seats >= seats_requested:
            print("Confirming a seat")
            print("Processing the payment")
            print("Printing the ticket")
            self.__available_seats -= seats_requested
        else:
            print("Sorry, no seats available")

        # self.__lock.release()


b = BookMyBus(10)
t1 = Thread(target=b.buy, args=([3]), name="Thread 1")
t2 = Thread(target=b.buy, args=([4]), name="Thread 2")
t3 = Thread(target=b.buy, args=([3]), name="Thread 3")

t1.start()
t2.start()
t3.start()
