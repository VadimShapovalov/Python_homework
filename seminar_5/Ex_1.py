# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Главный абв вопрос, еслиабв который ставит абв перед ниабвми нами будущее - это кого  сожратьабв туда впустить абв'


def del_words(txt):
    txt = list(filter(lambda x: 'абв' not in x, txt.split()))
    return ' '.join(txt)

text = del_words(text)
print(text)
