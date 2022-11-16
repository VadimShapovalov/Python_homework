"""
Задание 6.

Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.

При сдаче задания в папке должен лежать текстовый файл!
"""
import chardet

# функция для перекодировки в нужный формат. Здесь utf-8.
def universal_recod():
    with open('test_file.txt', 'rb') as my_file:
        in_bytes = my_file.read()
    detectend = chardet.detect(in_bytes)

    encoding = detectend['encoding']
    my_text = in_bytes.decode(encoding)
    with open('test_file_2.txt', 'w', encoding= 'utf-8') as my_file:
        my_file.write(my_text)


universal_recod()
# теперь ошибки не будет, даже если изначально была другая кодировка
with open('test_file.txt', encoding='utf-8') as my_file:
    text = my_file.read()
print(text)
