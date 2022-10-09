# Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.

def poly_sum(name_1: str, name_2: str):
    with open(name_1, 'r', encoding = 'utf-8') as my_f_1, \
        open(name_2, 'r', encoding = 'utf-8') as my_f_2:
        first = my_f_1.readlines()
        second = my_f_2.readlines()

        if len(first) == len(second):
            with open('sum_poly.txt', 'a', encoding = 'utf-8') as my_f_3:
                for i, v in enumerate(first):
                    my_f_3.write(f'{v[: -4]} + {second[i]}')
        else:
            print('Содержимое файла не совпадает.')
# poly_sum(input('Введите название файла "text_1.txt": '), input('Введите название файла "text_2.txt": '))
poly_sum('poly_1.txt', 'poly_2.txt')
