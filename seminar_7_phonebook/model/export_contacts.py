import csv
import exceptions.excepts as ex
import model.user_input as u_in

# чтение из файла и возврат данных в виде списка
def read_data(path):
	ex.read_file_except(path)
	with open(path, 'r', encoding='utf-8') as file:
		reader = csv.reader(file)
		data_list = []
		for row in reader:
			data_list.append(row)
		return data_list
			
# вывести информацию о всех контактах в списке
def show_all_contacts(path):
	list_contact = read_data(path)	# чтение данных из файла
	print('\n' * 20)
	print('=' * 61)
	print('||', 'имя'.center(15),  '||', 'фамилия'.center(15), '||', 'телефон '.center(15), ' ||')
	print('=' * 61)
	for person in list_contact:
		print('||', person[0].center(15),  '||', person[1].center(15), '||', person[2].center(15), '||')
	print('=' * 61)


# вывод информации о одтельно взятом контакте по имени и фамилии
def show_selected_contact(path):
	list_contact = read_data(path)	# чтение данных из файла
	print('Введите параметры поиска: ')
	name = u_in.check_input_string('Имя')	# ввод данных контакта 'имя'
	surname = u_in.check_input_string('Фамилия')	# ввод данных контакта 'фамилия'
	
	for person in list_contact:	# поиск контакта в полученном списке
		if name.lower() == person[0].lower() and surname.lower() == person[1].lower():
			index = list_contact.index(person)	# получаем индекс контакта
			print('\n' * 20)
			print('=' * 60)
			print('||', person[0].center(15),  '||', person[1].center(15), '||', person[2].center(15), ' ||')
			print('=' * 60)
			return
	print('Контакт : {} {} не найден.'.format(surname, name))
