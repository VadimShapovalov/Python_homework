# Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.

num = int(input('Введите число: '))
list = []
sum = 0
for i in range(1, num + 1):
    value = (1 + 1 / i)** i
    n = round(value, 2)
    list.append(n)
    sum += n
print(list)
print(sum)
