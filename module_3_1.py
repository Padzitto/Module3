calls = 0  # Создать переменную calls = 0 вне функций.


# Создаем функцию count_calls, подсчитывающую вызовы остальных функций.
# Эта функция должна вызываться в остальных двух функциях
def count_calls():
    global calls  # Для использования глобальной переменной внутри функции - оператор global.
    calls = calls + 1  # начинает отсчет


# Создаем функцию string_info принимает аргумент - строку
# и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(string):
    count_calls()  # вызываем функцию подсчета вызова функций
    return (len(string), string.upper(), string.lower())


# Создаем функцию is_contains принимает два аргумента: строку и список,
# и возвращает True, если строка находится в этом списке, False - если отсутствует
def is_contains(string, list):
    count_calls()  # вызываем функцию подсчета вызова функций
    string = string.upper()  # Пренебрегаем Регистром строки при проверке: UrbaN ~ URBAN.
    for i in list:  # привести и искомую строку и все строки в списке в один регистр.
        if string == i.upper():  # Ищем наличие строки (string) в списке (list)
            return True  # если есть, то верно True
    return False  # False - если отсутствует


# Пример выполняемого кода:
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)