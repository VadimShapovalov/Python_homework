# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def list_numbers(count: int):
    list_num = sample(range(-5, 6), count)
    print(list_num)
    return list_num

def multipl_pairs(list_num: list):
    res_list = []
    length_list = len(list_num)
    
    for i in range(length_list // 2):
        res_list.append(list_num[i] * list_num[length_list - i - 1])
    if length_list % 2:
            res_list.append(list_num [length_list // 2] * 2)
    print(res_list)
# Из условия не совсем понял, что делать со срединным элементом при нечетном количество чисел.
# Решил, что буду умножать его на самого себя и выводить в конце списка.

multipl_pairs(list_numbers(int(input('Введите количество чисел в списке: '))))
