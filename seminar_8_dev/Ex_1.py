"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:

    def __init__(self, *args):
        self.lst_of_lst = list(args)

    def __str__(self):
        matrix = '\n---------\n'.join(str(i) for i in self.lst_of_lst)
        matrix = matrix.replace('[', '').replace(']', '').replace(',', '  ')
        return matrix

    def __add__(self, other):
        line_sum = []
        sum_of_matrix = []
        for i in range(len(self.lst_of_lst)):
            for j in range(len(self.lst_of_lst[i])):
                line_sum.append(self.lst_of_lst[i][j] + other.lst_of_lst[i][j])
            sum_of_matrix.append(line_sum)
            line_sum = []
        sum_of_matrix = '\n-----------\n'.join(map(str, sum_of_matrix))
        sum_of_matrix = sum_of_matrix.replace('[', '')\
        .replace(']', '').replace(',', ' ')
        return sum_of_matrix


matrix_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
matrix_2 = Matrix([9, 8, 7], [6, 5, 4], [3, 2, 1])
print(f'Первая матрица:\n{matrix_1}')
print()
print(f'Вторая матрица:\n{matrix_2}')
print()
print(f'Сумма матриц:\n\n{matrix_1 + matrix_2}')
print()
