
def find_odds(lst: list):  
    lst_odds = []
    for i in lst:
        if i % 2 == 1:
           lst_odds.append(i)
    return lst_odds

# print(find_odds([4, 2, 9, 18, 20]))

def equals_or_not(a, b):
    if a == b:
        return a
    else:
        return None

# print(equals_or_not(5, 5))

def copy_function(a):
    b = a
    return b


def all_is_123(num):
    a = 123
    num = a
    return a

# Пример использования функции zip.Данны спискок имен и список номеров пользователей, необходимо их соединить в массив кортежей

def create_tuple(user_num: list, user_names: list):
    users_lst = list(zip(users_num, users_names))
    return users_lst

users_num = [1, 2, 3, 4, 5]
users_names = ['Вадим', 'Дмитрий', 'Марина', 'Екатерина', 'Максим']
# print(create_tuple(users_num, users_names))

