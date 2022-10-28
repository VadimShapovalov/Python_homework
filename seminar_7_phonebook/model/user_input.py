from logger import logs


# ввод данных пользователем
def input_data():
	name = check_input_string('имя')
	surname = check_input_string('фамилия')
	phone = check_input_digit('телефон')
	return [name, surname, phone]

# ввод данных и проверка строковых данных(оптимизация кода)
def check_input_string(desc: str):
	while True:
		val = input('Введите данные в поле "{}": '.format(desc))
		if len(val) < 3 or val.isspace() or not val.isalpha():
			print('поле "{}" должно быть больше 3 БУКВ и не пустым.'.format(desc))
			logs.input_logger('Пользователь ввел некорректные данные')
			continue
		return val.capitalize()

# ввод данных и проверка числовых данных(оптимизация кода) 
# и запись номера телефона в формате +1-(234)-567-89-01
def check_input_digit(desc: str):
	while True:
		val = input('Введите данные в поле "{}" (10 цифр номера, без 7 или 8): '.format(desc))
		if not val.isdigit() or val.isspace() or len(val)<10:
			print('В поле "{}" должны быть только цифры, \nоно должно быть не пустым \nи содержать ровно 10 цифр.'.format(desc))
			logs.input_logger('Пользователь ввел некорректные данные')
			continue
		val_ls = ''.join(filter(str.isdigit, val))
		return '+7-({})-{}-{}-{}'.format(val_ls[0:3], val_ls[3:6], val_ls[6:8], val_ls[8:10])
	
# проверка ввода числа для пользовательского меню
def choice_menu_input(max_range):
	while(True):
		i = input("Выберите один из вариантов работы: ")
		if i.isdigit() and 1 <= int(i) <= max_range:
			return int(i)
		print("Вам надо ввести число")
		logs.input_logger('Пользователь ввел некорректные данные')
