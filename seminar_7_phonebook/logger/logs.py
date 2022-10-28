from datetime import datetime as dt

# логирование ошибочного ввода данных пользователем
def input_logger(data):
    time = dt.now().strftime('%D  %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write(f'{data}, {time} \n')

# логирование выбранной операции
def oper_logger(data): 
    time = dt.now().strftime('%D  %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{}   Выбранная операция: {}\n'.format(time, data))
        file.write('=' * 30)
        file.write('\n')
