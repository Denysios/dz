def int_func(word):
    """Программа переводит первую букву слова в заглавную, если слово состоит из латинских букв нижнего регистра"""
    latin = 'abcdefghijklmnopqrstuvwxyz'
    return word.title() if not set(word).difference(latin) else False


# def int_func(word):
#        """Программа переводит первую букву слова в заглавную, если слово состоит из латинских букв нижнего регистра"""
#     for y in word:
#         if not chr(122) > y >= chr(97):
#             return
#     return word.title()


words = input('Введите слова через пробел, состоящие из маленьких латинских букв: ').split(' ')
words_str = ''
try:
    for i in words:
        words_str += ' ' + int_func(str(i))
except TypeError as err:
    print('Введены некорретные данные', err)
print(words_str)
