# Задание 2.
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
# Пример:
# Введите время в секундах: 3600
# Время в формате ч:м:с - 1.0 : 60.0 : 3600


second = int(input('Введите время в секундах: '))
minute = float(round(second/3600, 2))
hour = float(round(second/60, 2))
print(f'Время в формате ч:м:с - {minute} : {hour} : {second}')
#print(f'Время в формате ч:м:с - {round(second/3600, 2)} : {round(second/60, 2)} : {second}') второй вариант