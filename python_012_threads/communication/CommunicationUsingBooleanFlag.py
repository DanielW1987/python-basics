from threading import *
from time import *


class Producer:

    def __init__(self):
        self.__products = []
        self.__orders_placed = False

    def produce(self):
        for i in range(1, 5):
            self.__products.append("Product {}".format(i))
            sleep(1)
            print("Item added")
        self.__orders_placed = True

    def is_orders_placed(self) -> bool:
        return self.__orders_placed

    def get_products(self) -> list:
        return self.__products


class Consumer:

    def __init__(self, producer: Producer):
        self.__producer = producer

    def consume(self):
        while self.__producer.is_orders_placed() is False:
            sleep(0.2)

        print("Orders shipped {}".format(self.__producer.get_products()))


p: Producer = Producer()
c: Consumer = Consumer(p)

t1 = Thread(target=p.produce())
t2 = Thread(target=c.consume())

t1.start()
t2.start()
