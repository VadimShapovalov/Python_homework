import sys
import os
import logger.logs as log
import user_interface.interface as us_if
import model.user_input as inp
import model.contact_actions_handler as cah
import model.import_contacts as imp_c
import model.export_contacts as exp


path = 'list_contact'


# запуск приложения
def run():
	print('=' * 50)
	print('Добро пожаловать в наш телефонный справочник')
	
	while (True):
		us_if.main_menu()	# основное меню
		i = inp.choice_menu_input(4)	# ввод выбора действия
		
		if i == 1:
			us_if.menu_contact_actions()	# меню действий с контактов(создание/удаление)
			i = inp.choice_menu_input(4)	# ввод выбора действия
			if i == 1:
				log.oper_logger('Создание контакта')
				print('-' * 50)
				print('Вы выбрали "Создать контакт"')
				print('-' * 50)
				cc_list = cah.create_contact()	# создание контакта
				print('=' * 60)
				print('||', cc_list[0].center(15), '||', cc_list[1].center(15), '||',
										cc_list[2].center(15), '||')
				print('=' * 60)
				imp_c.save_data(cc_list, 'a')	# сохранение данных о контакте в файл
			elif i == 2:
				log.oper_logger('Удаление контакта')
				print('-' * 50)
				print('Вы выбрали "Удалить контакт"')
				print('-' * 50)
				cah.delete_contact(path)	# удаление контакта
			elif i == 3:
				log.oper_logger('Возврат в главное меню')
				print('-' * 50)
				print("Вернуться в главное меню")
				print('-' * 50)
				continue
			elif i == 4:
				log.oper_logger('Выход из программы')
				print('-' * 50)
				print("Программа завершила работу")
				print('-' * 50)
				sys.exit()

		elif i == 2:
			us_if.export_menu()	# меню экспорта контактов из файла
			i = inp.choice_menu_input(4)
			if i == 1:
				log.oper_logger('Вывод всех данных')
				print('-' * 50)
				print('Вы выбрали "Вывод всех данных"')
				print('-' * 50)
				exp.show_all_contacts(path)	# показать все контакты
			elif i == 2:
				log.oper_logger('Вывод информации о контакте')
				print('-' * 50)
				print('Вы выбрали "Вывод информации о контакте"')
				print('-' * 50)
				exp.show_selected_contact(path)	# показать отдельно взятый контакт по имени и фамилии
			elif i == 3:
				log.oper_logger('Возврат в главное меню')
				print('-' * 50)
				print("Вернуться в главное меню")
				print('-' * 50)
				continue
			elif i == 4:
				log.oper_logger('Выход из программы')
				print('-' * 50)
				print("Программа завершила работу")
				print('-' * 50)
				sys.exit()

		elif i == 3:
			us_if.import_menu()	# меню импорта в .csv формат
			i = inp.choice_menu_input(3)
			if i == 1:
				log.oper_logger('Импорт в файл')
				print('-' * 50)
				print('Вы выбрали "Импортировать в файл"')
				print('-' * 50)
				user_path = input('Введите название файла: ')	# ввод названия нового файла
				imp_c.import_to_csv(user_path)	# сохранение данных в .csv файл
				if os.path.exists(user_path + '.csv'):	# проверка, что файл успешно ипортирован
					print('Файл успешно скопирован.')
					print('-' * 50)
			elif i == 2:
				log.oper_logger('Возврат в главное меню')
				print('-' * 50)
				print("Вернуться в главное меню")
				print('-' * 50)
				continue
			elif i == 3:
				log.oper_logger('Выход из программы')
				print('-' * 50)
				print("Программа завершила работу")
				print('-' * 50)
				sys.exit()
				
		elif i == 4:
			log.oper_logger('Выход из программы')
			print('-'*50)
			print("Программа завершила работу")
			print('-'*50)
			sys.exit()
		