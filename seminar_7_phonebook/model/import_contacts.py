import csv
from encodings import utf_8
import shutil


# сохранение данных в файл
def save_data(data, rec_mode):
	with open('list_contact', rec_mode, encoding="utf_8", newline='') as file:
		writer = csv.writer(file)
		writer.writerow(data)

# перезапись существуещего файла
def rewrite(data_list, rec_mode):
	with open('list_contact', rec_mode, encoding="utf_8", newline='') as file:
		for person in data_list:
			for text in person:
				if person.index(text) == (len(person) - 1):
					file.write(text)
					break
				file.write(text + ',')
			file.write('\n')

# импорт в формат .csv
def import_to_csv(file_name):
	shutil.copy('list_contact', f'{file_name}.csv')
