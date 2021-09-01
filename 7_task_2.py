# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Apparel(ABC):

    def __init__(self, measure):
        self.measure = measure

    @property
    @abstractmethod
    def consump(self):
        pass

    def __add__(self, other):
        return self.consump + other.consump

class Coat(Apparel):

    @property
    def consump(self):
        return self.measure / 6.5 + 0.5

class Costume(Apparel):

    @property
    def consump(self):
        return 2 * self.measure + 0.3

coat = Coat(100)
costume = Costume(50)

print(coat + costume)
