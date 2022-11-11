# класс создающий дескриптор
class CorrectSize:
    def __set__(self, instance, value):
        if  value < 30:
            raise ValueError('Фабрика не шьет такие пальто.')
        instance.__dict__[self.attr] = value

    def __set_name__(self, owner, attr):
        self.attr = attr


class Clothes():

    size_of_coat = CorrectSize()

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

clothes = Clothes(20, 200)

print(clothes.fabric_coat_calculation)
