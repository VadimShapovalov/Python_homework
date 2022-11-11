from random import randint

# класс создающий дескриптор
class OverSpeed:
    def __set__(self, instance, value):
        if value > 450:
            raise ValueError('Машина не может развить такую скорость!')
        instance.__dict__[self.attr] = value

    def __set_name__(self, owner, attr):
        self.attr = attr


class Car:

    speed = OverSpeed()

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed != 0:
            return (f'Ваш {self.color} {self.name} едет.')

    def stop(self):
        if self.speed == 0:
            return (f'Ваш {self.color} {self.name} остановился.')
        else:
            return ('Все в порядке.')

    def turn(self):
        rand_turn = randint(1, 3)
        if rand_turn == 1:
            return (f'Ваш {self.color} {self.name} едет прямо.')
        elif rand_turn == 2:
            return (f'Ваш {self.color} {self.name} повернул направо.')
        else:
            return (f'Ваш {self.color} {self.name} повернул налево.')

    def show_speed(self):
        return (f'Скорость {self.color} {self.name}: {self.speed} км/ч')

obj_Car = Car(500, 'red', 'Lada', False)
print(obj_Car.speed)
