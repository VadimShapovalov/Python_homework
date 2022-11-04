"""
Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property
Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""
from abc import ABC, abstractmethod

class AbstractClass(ABC):

    @abstractmethod
    def fabric_coat_calculation(self):
        pass

    @abstractmethod
    def fabric_suit_calculation(self):
        pass

    @abstractmethod
    def fabric_total_calculation(self):
        pass

class Clothes(AbstractClass):

    def __init__(self, size_of_coat, height_of_suit):
        self.size_of_coat = size_of_coat
        self.height_of_suit = height_of_suit

    @property
    def fabric_coat_calculation(self):
        fabric_coat = self.size_of_coat / 6.5 + 0.5
        return f'Расход ткани на пальто: {round(fabric_coat, 2)}'

    def fabric_suit_calculation(self):
        fabric_suit = 2 * self.height_of_suit + 0.3
        return f'Расход ткани на костюм: {round(fabric_suit, 2)}'

    @property
    def fabric_total_calculation(self):
        fabric_total = \
        f'Общий расход ткани: {round((self.size_of_coat / 6.5 + 0.5) + (2 * self.height_of_suit + 0.3), 2)}'
        return fabric_total

clothes = Clothes(50, 200)

print(clothes.fabric_suit_calculation())
print(clothes.fabric_coat_calculation)
print(clothes.fabric_total_calculation)