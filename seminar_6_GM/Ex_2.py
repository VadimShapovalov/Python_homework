# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

def list_orig(num):
    return [i for i in range(20, num + 1) if not i % 20 or not i % 21]

print(list_orig(int(input('Введите число больше 20-ти: '))))
