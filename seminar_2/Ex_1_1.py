# Вариант №1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input('Введите вещественное число: '))
sum = 0
length = len(str(num)) - 2
num *= 10 ** length
while num:
    sum += num % 10
    num //= 10
print(int(sum))
