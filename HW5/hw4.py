# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4


def sum_a_b(a, b):
    if b == 0:
        return a
    else:
        return 1 + sum_a_b(a, b - 1)
n1 = int(input("Введите первое число: "))
n2 = int(input("Введите втроре число: "))
print(sum_a_b(n1, n2))

