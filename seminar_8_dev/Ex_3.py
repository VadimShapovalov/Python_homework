"""
Задание 3.
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка (Cell).
В его конструкторе инициализировать параметр (quantity),
соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
"""
class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'{self.quantity}'

    def __add__(self, other):
        return f'Сумма клеток равна: {Cell(self.quantity + other.quantity)}'

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return f'Разность клеток равна: {Cell(self.quantity - other.quantity)}'
        else:
            return 'Внимание! Операция невозможна в виду отрицательного значения.'

    def __mul__(self, other):
        return f'Произведение клеток равно: {Cell(self.quantity * other.quantity)}'

    def __truediv__(self, other):
        if other.quantity != 0:
            return f'Деление клеток равно: {Cell(self.quantity // other.quantity)}'
        else:
            return 'Ошибка! Нельзя делить на ноль!'

cell_1 = Cell(24)
cell_2 = Cell(5)

print(cell_1 + cell_2)
print()

print(cell_1 - cell_2)
print()

print(cell_1 * cell_2)
print()

print(cell_1 / cell_2)
print()  
