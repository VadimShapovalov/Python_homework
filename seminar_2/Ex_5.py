#  Реализуйте алгоритм перемешивания списка. 

from random import randrange

num = int(input('Введите число обозначающее размер списка: '))
list_original = list(range(num))
length = len(list_original)
print(list_original)
list_second = list_original
for i in range(length):
    num_1 = randrange (length)
    num_2 = randrange (length)
    list_second[num_1], list_second[num_2] = list_second[num_2], list_second[num_1]
print(list_second)
