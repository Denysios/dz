# Вариант 1
def my_func(x, y):
    """Функция принимает 2 аргумента, и возводит x в степень y"""
    try:
        return abs(int(x)) ** int(y) if int(y) < 0 else print('Второе число не отрицательное')
    except ValueError as error:
        print('Вы ввели не корректные данные - ', error)
    except TypeError as error:
        print('Вы ввели не корректные данные - ', error)


plus_num = input('Введите действительное положительное число: ')
minus_num = input('Введите целое отрицательное число: ')
print(my_func(plus_num, minus_num))

# Вариант 2
# def my_func(x, y):
#     """Функция принимает 2 аргумента, и возводит x в степень y"""
#     try:
#         result = 1 / abs(int(x))
#         for _ in range(abs(int(y) + 1)):
#             result *= 1 / abs(int(x))
#         print(pow(10, -5))
#         return result
#         #return abs(int(x)) ** int(y) if int(y) < 0 else print('Второе число не отрицательное')
#     except ValueError as error:
#         print('Вы ввели не корректные данные - ', error)
#     except TypeError as error:
#         print('Вы ввели не корректные данные - ', error)
#
#
# plus_num = input('Введите действительное положительное число: ')
# minus_num = input('Введите целое отрицательное число: ')
# print(my_func(plus_num, minus_num))
