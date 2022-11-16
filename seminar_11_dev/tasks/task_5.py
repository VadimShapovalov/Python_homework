"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import chardet
import subprocess

# пинг Яндекса с преобразованием из байтов в строки
ARGS = ['ping', 'yandex.ru']
YANDEX_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YANDEX_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

# пинг Youtube.com с преобразованием из байтов в строки
ARGS = ['ping', 'youtube.com']
YOUTUBE_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YOUTUBE_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
    