# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def users_data():
    name = input('Введите своё имя: ')
    surname = input('Введите свою фамилию: ')
    birthday = input('Дата рождения: ')
    city = input('Город проживания: ')
    email = input('Укажите эл. почту: ')
    phone = input('Введите номер телефона: ')
    return f"Имя - {name}, Фамилия - {surname}, Дата рождения - {birthday}, Город проживания - {city},"\
    f"Эл. почта - {email}, Номер телефона - {phone}"

print(users_data())