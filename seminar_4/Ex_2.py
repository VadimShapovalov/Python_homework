# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def find_prime_num(num):

    prime_num = 2
    list_num = []
    temp = num
    while prime_num <= temp:
        if not temp % prime_num:
            list_num.append(prime_num)
            temp //= prime_num
            prime_num = 2
        else:
            prime_num += 1
    print(f'Простоые множители числа {num} приведены в списке {list_num}')

find_prime_num(int(input('Введите число: ')))
