"""
Задание 5.
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return ('Запуск отрисовки.')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f'Запуск отрисовки {self.title}.')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f'Запуск отрисовки {self.title}.')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f'Запуск отрисовки {self.title}.')


obj_origin = Stationery('канцелярская принадлежность')
obj_pen = Pen('ручкой')
obj_pencil = Pencil('карандашом')
obj_handle = Handle('маркером')

print(obj_origin.draw())
print(obj_pen.draw())
print(obj_pencil.draw())
print(obj_handle.draw())
