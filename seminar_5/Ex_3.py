# Создайте программу для игры в ""Крестики-нолики"".

from random import choice, randint

board = [i for i in range(1, 10)]
player1 = input('Первый игрок, пожалуйста, представтесь!\n ')
player2 = input('Второй игрок, пожалуйста, представтесь!\n ')
players = [player1, player2]

messages = ['пожалуйста, ходите', ' пожалуйста, делайте Ваш ход!', 'Ваш ход!']


def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")


def player_choice(player_token):
    val = False
    count = 0
    while not val:
        try:
            player_answer = int(
                input(f'Выберите клетку для {player_token}: '))
        except ValueError:
            print('Такой клетки нет! Попробуйте еще раз!')
            continue
        if 1 <= player_answer <= 9:
            if (str(board[player_answer - 1]) not in 'X' and 'O'):
                board[player_answer - 1] = player_token
                val = True
            else:
                print('Эта клетка уже занята! Выберите другую!')
        else:
            print('Некорректный ввод! Введите число от 1 до 9!')


def check_win(board):
    solutions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for el in solutions:
        if board[el[0]] == board[el[1]] == board[el[2]]:
            return board[el[0]]
    return False


def game(board, players, messages):
    count = 0
    counter = 0
    player_draw = randint(1, 2)
    win = False
    while not win:
        draw_board(board)
        if player_draw == 1:
            print(f'{players[count % 2]}, {choice(messages)}')
        else:
            print(f'{players[not count % 2]}, {choice(messages)}')
        if counter % 2 == 0:
            player_choice('X')
        else:
            player_choice('O')
        counter += 1
        if counter > 4:
            check_true = check_win(board)
            if check_true:
                print(f'Поздравляем {players[count % 2]}, Вы выиграли!')
                win = True
            if counter == 9:
                print('Ничья!')
                break
        count += 1
        draw_board(board)


game(board, players, messages)
