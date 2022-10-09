# Вычислить число c заданной точностью d

from msilib import MSIMODIFY_INSERT_TEMPORARY

def accuracy(num):

    k = 1
    my_Pi = 0

    for i in range(1000000):
        if i % 2 == 0:
            my_Pi += 4 / k
        else:
            my_Pi -= 4/k
        k += 2

    # print(my_Pi)
    print(f'Number with precision {num}: {str(my_Pi)[: len(num)]}')

accuracy(input('Enter the precision of number in the format 0.0001: '))
