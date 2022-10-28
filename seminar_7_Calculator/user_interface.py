import logg


def main_menu(i):
	logg.type_num_logger(i)
	if i == "Welcome":
		print('=' * 30)
		print('Здравствуйте')
	elif i == "Menu":
		print('=' * 30)
		print('Варианты работы программы')
		print('1. Калькулятор для работы с рациональными числами')
		print('2. Калькулятор для работы с комплексными числами')
		print('3. Выход из программы')
		print('=' * 30)
		
def choice_actions_menu(i):
	logg.type_num_logger(i)
	print('=' * 30)
	print('Варианты работы программы')
	print('1. Введите "+" чтобы a+b')
	print('2. Введите "-" чтобы a-b')
	print('3. Введите "*" чтобы выбрать действия умножения')
	print('4. Введите "/" чтобы выбрать действие деления')
	print('5. Выход из программы')
	print('=' * 30)

def error():
	print('=' * 30)
	print('------ Ошибка -------')
	print('=' * 30)
	
def choice_mult_actions(i):
	logg.type_num_logger(i)
	print('---------------------------------------------')
	print('Варианты работы программы')
	print('1. Введите "1" чтобы a*b')
	print('2. Введите "2" чтобы a**b')

def choice_div_actions(i):
	logg.type_num_logger(i)
	print('---------------------------------------------')
	print('Варианты работы программы')
	print('1. Введите "1" чтобы a/b')
	print('2. Введите "2" чтобы a//b')
	print('3. Введите "3" чтобы a"%"b')
	
def end_menu(i):
	logg.type_num_logger(i)
	print('----------------------------------------------')
	print('Выберите дальнейшее действие')
	print('1. Выход в главное меню')
	print('2. Выход из программы')
