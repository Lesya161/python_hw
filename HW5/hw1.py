# Задание 1. Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна
# запрашивать новые данные для вычислений. Завершение программы должно
# выполняться при вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.
# Подсказка:
# Вариант исполнения:
# - условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
# - условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
# Решите через рекурсию. В задании нельзя применять циклы.
# Пример:
# Введите операцию (+, -, *, / или 0 для выхода): +
# Введите первое число: 214
# Введите второе число: 234
# Ваш результат 448
# Введите операцию (+, -, *, / или 0 для выхода): -
# Введите первое число: вп
# Вы вместо трехзначного числа ввели строку (((. Исправьтесь
# Введите операцию (+, -, *, / или 0 для выхода):

def mat_operations(op, n1, n2):
    while True:
        op = input("Введите операцию или 0 для выхода: ")
        if op == "0":
            break
        if op == "+" or op == "-" or op == "*" or op == "/":
            n1 = int(input("Введите первое число: "))
            n2 = int(input("Введите второе число: "))

            if op == "+":
                print("Ваш результат ", n1 + n2)
                return mat_operations(op, n1, n2)
            elif op == "*":
                print("Ваш результат ", n1 * n2)
                return mat_operations(op, n1, n2)
            elif op == "-":
                print("Ваш результат ", n1 - n2)
                return mat_operations(op, n1, n2)
            elif op == "/":
                if n2 == 0:
                    print("На 0 дельть нельзя")
                    continue
                else:
                    print("Ваш результат ", n1 / n2)
                    return mat_operations(op, n1, n2)
        else:
            print("Ошибка, введите (+, -, *, / или 0 для выхода)")
            continue

print(mat_operations(2, 1, 4))