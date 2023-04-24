"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
def transformation_bytes(array):
    array_word = []
    for el in array:
        array_word.append(el.encode('utf-8'))
    return array_word

def transformation_word(array):
    array_word = []
    for el in array:
        array_word.append(el.decode('utf-8'))
    return array_word

word = ['разработка', 'администрирование', 'protocol', 'standard']
print('Байты')
bytes_words = transformation_bytes(word)
for element in bytes_words:
    print(element)
print('Буквы')
more_words = transformation_word(bytes_words)
print(more_words)