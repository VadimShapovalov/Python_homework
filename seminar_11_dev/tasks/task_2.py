"""
Задание 2.
Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
"""
#  для записи в байтовом формате достаточно добавить букву "b" (если все используемые символы есть в кодировке ASCII)

a = b'class'
b = b'function'
c = b'method'

lst_b = [a, b, c]

# метод определяющий тип, содержание и длинну переменных
def show_type_length(lst_b):
    for i in range(len(lst_b)):
        print(type(lst_b[i]), lst_b[i])
        print(f'Длина переменной {lst_b[i]}: {len(lst_b[i])}')

show_type_length(lst_b)
