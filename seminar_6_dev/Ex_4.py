# Пример использования функции enumerate.
# Необходимо пронумеровать элементы списка
from random import randint

lst = [randint(1, 9) for i in range(4)]
print(f"Начальный список: {lst}")

# Без использования функции enumerate
for i in range(len(lst)):
    print(f'Элемент списка: {lst[i]}, индекс элемента: {i}')

print('-------------------------------------')

# С использованием функции enumerate
for i, el in enumerate(lst):
    print(f'Элемент списка: {el}, индекс элемента: {i}')
