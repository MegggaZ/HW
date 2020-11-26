from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__color = (('red', 7), ('yellow', 2), ('green', 7))

    def work(self):
        for color, sec in cycle(self.__color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)


tr_l = TrafficLight()
tr_l.work()
