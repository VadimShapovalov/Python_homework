# Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.

from random import sample

def more_then(num):
    lst_nums = sample(range(1, 21), num)
    print(lst_nums)
    return [lst_nums[i] for i in range(1, len(lst_nums)) if lst_nums[i] > lst_nums[i - 1]]

print(more_then(int(input('Введите размер списка: '))))
