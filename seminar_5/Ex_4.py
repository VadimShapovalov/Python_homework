# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('decode_file.txt', 'w') as data:
    data.write('AABBBCCCC')

with open('decode_file.txt', 'r') as data:
    decode_txt = data.read()


def encode_rle(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
    return encoding


encode = encode_rle(decode_txt)
print(f'Закодированные данные: {encode}')

with open('encode_file.txt', 'w') as data:
    data.write(f'{encode}')

with open('encode_file.txt', 'r') as data:
    encode_txt = data.read()


def decode_rle(data):
    decoding = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decoding += char * int(count)
            count = ''
    return decoding


decode = decode_rle(encode_txt)