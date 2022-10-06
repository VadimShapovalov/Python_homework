# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def convert_bin(num: int):
    list_num = []

    while num > 0:
        list_num.insert(0, num % 2)
        num //= 2
    print(*list_num, sep = "")

convert_bin(int(input('Введите число: ')))
