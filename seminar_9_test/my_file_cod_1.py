# Задайте список, состоящий из произвольных чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

def sum_odd_position(list_num: list):
    sum_num = 0
    for i in range(0, len(list_num), 2): # считаю сумму на нечетных позициях, а не индексах, поэтому стоит "0"
        sum_num += list_num[i]
    return(sum_num)

#print(sum_odd_position([1, 2, 3, 4 , 5, 6]))

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:  - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input('Введите число: '))
def sum_mult(num):
    value = 1
    lst = []
    for i in range(1, num + 1):
        value *= i
        lst.append(value)
    return lst

# print(sum_mult(5)) 

def Is_square(side_a, side_b):
    if side_a == side_b:
        return True
    else:
        return False

# print(Is_square(5, 5))
    
def find_even(lst: list):  
    lst_even = []
    for i in lst:
        if i % 2 == 0:
           lst_even.append(i)
    return lst_even


def check_odd(num):
    if num % 2 == 1:
        return num
    else:
        return None

# print(check_odd(6))
