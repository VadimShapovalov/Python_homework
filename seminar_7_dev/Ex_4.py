"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
from random import randint


class Car:
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

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(
                f'Вы превысили скорость!. Ваша скорость составила: {self.speed} км/ч.')
            is_police = True
            if is_police:
                print('Вас остановила полиция.')
                self.speed = 0
                return (f'Скорость {self.color} {self.name}: {self.speed} км/ч.')
        else:
            return (f'Скорость {self.color} {self.name}: {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(
                f'Вы превысили скорость! Ваша скорость составила: {self.speed} км/ч.')
            is_police = True
            if is_police:
                print('Вас остановила полиция.')
                self.speed = 0
                return (f'Скорость {self.color} {self.name}: {self.speed} км/ч.')
        else:
            return (f'Скорость {self.color} {self.name}: {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


obj_town = TownCar(60, 'красный', 'Mustang', False)
obj_sport = SportCar(110, 'желтый', 'Porshe', False)
obj_work = WorkCar(50, 'черный', 'Ford', False)
obj_police = PoliceCar(40, 'синяя', 'полицейская Lada', False)

# Вывод результата работы методов для объекта класса TownCar
print(obj_town.go())
print(obj_town.turn())
print(obj_town.show_speed())
print(obj_town.stop())
print()

# Вывод результата работы методов для объекта класса SportCar
print(obj_sport.go())
print(obj_sport.turn())
print(obj_sport.show_speed())
print(obj_sport.stop())
print()

# Вывод результата работы методов для объекта класса WorkCar
print(obj_work.go())
print(obj_work.turn())
print(obj_work.show_speed())
print(obj_work.stop())
print()

# Вывод результата работы методов для объекта класса PoliceCar
print(obj_police.go())
print(obj_police.turn())
print(obj_police.show_speed())
print(obj_police.stop())
print()
