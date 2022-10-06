# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def diff_min_max(list_real_num: list):
    list_result = []
    for i in list_real_num:
        if i % 1 != 0:
            list_result.append(i % 1)
            list_result.sort()
    print(f'Разница между max и min дробной части элементов равна: {list_result[len(list_result)-1]-list_result[0]:.5f}')

list_real_num = [1.1, 1.2, 3.1, 5, 10.01]

diff_min_max(list_real_num)
