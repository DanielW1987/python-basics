from threading import *
from time import *


class Producer:

    def __init__(self):
        self.__products = []
        self.__condition = Condition()

    def produce(self):
        self.__condition.acquire()

        for i in range(1, 5):
            self.__products.append("Product {}".format(i))
            sleep(1)
            print("Item added")

        self.__condition.notify()
        self.__condition.release()

    def get_products(self) -> list:
        return self.__products

    def get_condition(self) -> Condition:
        return self.__condition


class Consumer:

    def __init__(self, producer: Producer):
        self.__producer = producer

    def consume(self):
        self.__producer.get_condition().acquire()
        self.__producer.get_condition().wait(timeout=0)
        print("Orders shipped {}".format(self.__producer.get_products()))
        self.__producer.get_condition().release()


p: Producer = Producer()
c: Consumer = Consumer(p)

t1 = Thread(target=p.produce())
t2 = Thread(target=c.consume())

t1.start()
t2.start()
