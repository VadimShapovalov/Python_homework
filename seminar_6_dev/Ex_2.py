# Пример использования map и lambda.
# 24.	Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# o	[1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint

n = int(input('Введите размер списка: '))

lst_int = [randint(11, 100) for i in range(1, n + 1)]

# Старое решение
# lst_float = []
# count = 0

# for i in lst_int:
#     count += 1
#     if count <= N:
#         float_num = i / 10
#         lst_float.append(float_num)

# print(f'Полученный список вещественных чисел: {lst_float}')

# lst_digit = []
# for i in range(len(lst_float)):
#     digit = lst_float[i] % 1
#     lst_digit.append(round(digit, 1))

# print(f'Дробная часть списка вещественных чисел: {lst_digit}')

# for i in range(len(lst_digit)):  
#     max_digit = max(lst_digit) 
#     min_digit = min(lst_digit)
#     res = round((max_digit - min_digit), 2)

# print(
#     f'Разница между макс. и мин. значением дробной части элементов: {res}')

# Новое решение:
lst = list(map(lambda x: x / 10, lst_int))
print(f'Список вещественных чисел: {lst}')

lst = list(map(lambda x: round(x % 1, 2), lst))
print(f'Дробная часть: {lst}')

result = round(max(lst) - min(lst), 2)
print(f'Разница между макс. и мин. значениями: {result}')
