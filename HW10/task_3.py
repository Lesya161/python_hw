"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
def bytes_words(array):
    array_word = []
    try:
        for el in array:
            array_word.append(bytes(el, 'ascii'))
    except UnicodeEncodeError:
        print("невозможно записать в байтовом типе с помощью маркировки b''")
    return array_word

words = ['attribute', 'класс', 'функция', 'type']
res = bytes_words(words)
print(res)