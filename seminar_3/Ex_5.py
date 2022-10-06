# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def neg_fib(num: int):
    a, b = 1, 1
    list_num = [0]
    for i in range(num):
        list_num.append(a)
        list_num.insert(0, a * (-1) ** i)
        a, b = b, b + a
    print(*list_num)

neg_fib(int(input('Введите число: ')))
