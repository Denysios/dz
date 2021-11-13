from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def calc_cloth(self):
        pass

    def __add__(self, other):
        return self.calc_cloth + self.calc_cloth


class Coat(Clothes):

    @property
    def calc_cloth(self):
        return round(self.param/6.5) + 0.3


class Suit(Clothes):

    @property
    def calc_cloth(self):
        return (2 * self.param + 0.3)/100


coat = Coat(58)
suit = Suit(240)
print(coat + suit)


# class Clothes:
#
#     def __init__(self, param: int):
#         self.param = param
#
#     def __str__(self):
#         return str(self)
#
#
# class Coat(Clothes):
#
#     def calc_size(self, param: int):
#         super().__init__(param)
#         self.param = param
#         return round(param/6.5 + 0.5, 2)
#
#
# class Suit(Clothes):
#
#     def calc_height(self, param: int):
#         super().__init__(param)
#         self.param = param
#         return int(2 * param + 0.3)
#
#
# a = Coat(40)
# b = Suit(240)
# print(b.calc_height(240))
# print(a.calc_size(40))
