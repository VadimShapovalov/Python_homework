"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

class Position(Worker):
    def __init__(self, name, surname, position, _income, wage, bonus):
        '''Определяет заничения новых атрибутов и наследует атрибуты от класса родителя'''
        super().__init__(name, surname, position, _income)
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}

    def get_full_name(self):
        return (f'\nФамилия: {self.surname}\nИмя: {self.name}\nДолжность: {self.position}')

    def get_total_income(self):
        total_income = self._income.get('wage') + self._income.get('bonus')
        return (f'Доход с учетом премии: {total_income} тыс. руб.')

obj = Position('Vadim', 'Shapovalov', 'Developer', None, 200, 100)
print(obj.get_full_name())
print(obj.get_total_income())
print()
print(f'Атрибут wage: {obj.wage}')
print(f'Атрибут bonus: {obj.bonus}')
print(f'Атрибут _income: {obj._income}')
print(f'Атрибут name: {obj.name}')
print(f'Атрибут surname: {obj.surname}')
print(f'Атрибут position: {obj.position}\n')
