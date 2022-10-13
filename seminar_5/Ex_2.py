# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import choice, randint

# Входные данные
n = 2021
m = 28
player1 = input('Первый игрок, пожалуйста, представтесь!\n ')
player2 = input('Второй игрок, пожалуйста, представтесь!\n ')
players = [player1, player2]

messages = ['cколько конфет Вы возьмете?', ' Ваша очередь брать конфеты!', 'Ваш ход!',
            'пожалуйста, берите конфеты.']


def candy_game(n, m, players, messages):
    count = 0
    player_draw = randint(1, 2)
    while n > 0:
        if player_draw == 1:
            print(f'{players[count % 2]}, {choice(messages)}')
            move = int(input())
        else:
            print(f'{players[(count + 1) % 2]}, {choice(messages)}')
            move = int(input())
        if move > n or move > m:
            print(
                f'Это слишком много, нельзя взять больше {m} конфет. Всего сейчас {n} конфет{letter}.')
            attempt = 3
            while attempt > 0:
                print(f'Попробуйте еще раз! У вас еще {attempt} попытки.')
                move = int(input())
                attempt -= 1
                if move < n and move <= m:
                    break
            else:
                return print('Очень жаль, у вас больше не осталось попыток. Игра окончена! :(')
        n -= move
        if (n % 10 == 1 or n == 1) and n != 11:
            letter = 'а'
        elif 1 < n % 10 <= 4 and n not in range(12, 15):
            letter = 'ы'
        else:
            letter = ''
        if n > 0:
            print(f'Осталось {n} конфет{letter}.')
        else:
            print('Конфеты кончились!')
        count += 1
    if player_draw == 1:
        return players[not count % 2]
    else:
        return players[count % 2]


winner = candy_game(n, m, players, messages)
if not winner:
    print('Победителей нет. Это ничья!')
else:
    print(f'Поздравляем {winner} с победой!')
    