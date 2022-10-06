# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def list_numbers(count: int):
    list_num = sample(range(-10, 10), count)
    print(list_num)
    return list_num

def sum_odd_position(list_num: list):
    sum_num = 0
    for i in range(0, len(list_num), 2): # ориентируюсь на пример в задании, где сумма на нечетных позициях, а не индексах, поэтому стоит "0"
        sum_num += list_num[i]
    print(sum_num)

sum_odd_position(list_numbers(int(input('Введите количество чисел: '))))
