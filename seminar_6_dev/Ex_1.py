# Пример использования list comprehension и lambda.
# 22.	Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# o	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from functools import reduce
from random import randint

n = int(input('Введите размер списка: '))
lst = [randint(1, 10) for i in range(1, n + 1)]
print(lst)

# Старое решение:

# odd_numbers = []
# for i in range(len(lst)):
#     if i % 2:
#         odd_numbers.append(lst[i])
# print(odd_numbers)

# res = 0
# for i in odd_numbers:
#     res += i
# print(res)

# Новое решение с применением list comprehension и lambda:
lst = [lst[i] for i in range(len(lst)) if i % 2]
print(lst)

result = reduce(lambda x, y: x + y, lst)
print(result)
