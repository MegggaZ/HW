from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, cloth):
        self.cloth = cloth

    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):

    @property
    def calc(self):
        return round((self.cloth / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calc(self):
        return round((2 * self.cloth) + 0.3)


coat = Coat(55)
suit = Suit(193)
print(coat.calc)
print(suit.calc)