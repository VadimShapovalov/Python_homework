import os
import sys

# проверка существования указанного файла
def read_file_except(file_path):
	if not os.path.exists(file_path):
		print(f'файл не найден или некорректно указан путь: {file_path}')
		sys.exit()
