# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

words = input('Введите несколько слов через пробел: ')
n = 1

for i in words.split():
    print(f'Строка {n}: {i[:10]}')
    n += 1
