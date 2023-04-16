# Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).
# Подсказка:
# На каждом шаге вам нужно 'доставать' из числа очередную цифру
# и смотреть является ли она четной или нечетной.
# При этом увеличиваем соответствующий счетчик
# Пока все числа не извлечены, рекурсивные вызовы продолжаем
# Условие завершения рекурсии - все числа извлечены
# Используем операции % //. Операции взятия по индексу применять нельзя.
# Решите через рекурсию. В задании нельзя применять циклы.
# Пример:
# Введите число: 123
# Количество четных и нечетных цифр в числе равно: (1, 2)

def even_odd(n, even = 0, odd = 0):
    if not n:
        return even, odd
    elif n % 2 == 1:
        odd += 1
    else:
        even += 1
    return even_odd(n // 10, even, odd)
n = int (input("Введите число: "))
print(f'Количество четных и нечетных чисел равно {even_odd(n)}')