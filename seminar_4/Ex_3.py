# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randrange

def list_rand_num(count: int):
    list_num = []
    for i in range(count):
        list_num.append(randrange(count))

    return list_num

def uniq_elem(list_num: list):
    result = []
    my_dict = {}.fromkeys(list_num, 0)

    for i in list_num:
        my_dict[i] +=1

    for k in my_dict:
        if my_dict[k] == 1:
            result.append(k)
    return result

all_list = list_rand_num(int(input('Введите количество чисел: ')))
print(all_list)
print(uniq_elem(all_list))
