# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

user_str = input('Введите предложение из нескольких слов: ').split()
for ind, i in enumerate(user_str, 1):
         print(ind, i[0:10])