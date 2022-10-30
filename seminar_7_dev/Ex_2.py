"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""
class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width, mass, thickness):
        self._length = length
        self._width = width
        self.mass = mass
        self.thickness = thickness

    def calc_asphalt_mass(self):
        result = self._length * self._width * self.mass * self.thickness
        return (f'Масса асфальта = {int(result)} кг = {int(result / 1000)} т')


obj_road = Road(20, 5000, 25, 0.05)
print(obj_road.calc_asphalt_mass())
