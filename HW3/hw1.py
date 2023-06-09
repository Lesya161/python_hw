# """
# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень
# """

season_year_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
season_year_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}

season_month = int(input("Введите месяц в виде целого числа: "))
if season_month > 12 or season_month < 1:
    print('Вы ввели неверное число, попробуйте еще раз.')
else:
    season_month = season_month - 1
    print(f'Это месяц в списке: {season_year_list[season_month]}')

season_month = int(input("Введите месяц в виде целого числа: "))
if season_month > 12 or season_month < 1:
    print('Вы ввели неверное число, попробуйте еще раз.')
else:
    print(f'Это месяц в словаре: {season_year_dict[season_month]}')

