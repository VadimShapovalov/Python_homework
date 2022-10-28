import model.user_input as u_in
import model.export_contacts as exp
import model.import_contacts as imp_c

# создание контакта
def create_contact():
	contact_list = u_in.input_data()	# ввод данных в виде списка
	return contact_list
	
# удаление контакта
def delete_contact(path):
	list_contact = exp.read_data(path)	# чтение файла со списком контактов
	print('Введите параметры удаления: ')
	name = u_in.check_input_string('Имя')	# ввод данных контакта 'имя'
	surname = u_in.check_input_string('Фамилия')	# ввод данных контакта 'фамилия'
	
	for person in list_contact:	# поиск контакта в полученном списке
		if name.lower() == person[0].lower() and surname.lower() == person[1].lower():
			index = list_contact.index(person)	# получаем индекс контакта
			list_contact.pop(index)	# удаляем контакт
			print('=' * 60)
			print(f'Контакт {person[0]} {person[1]} успешно удалён.')	# вывод результата удаления
			print('=' * 60)
			imp_c.rewrite(list_contact, 'w')	# перезаписываем в файл новый список, уже без удаленного контакта
			return
	print('Контакт : {} {} не найден.'.format(surname, name))
