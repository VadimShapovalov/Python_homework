# Пример использования функции filter.
from random import randint

lst = [randint(1, 10) for i in range(1, 10)]
print(f"Начальный список: {lst}")

# Вариант решения без функции filter

new_lst = []
for i in lst:
    if i % 2 == 0:
        new_lst.append(i)

print(f"Список четных элеметов без применения filter: {new_lst}")

# Новое решение
lst = list(filter(lambda x: not x % 2, lst))
print(f'Список четных элеметов c применением filter: {lst}')
