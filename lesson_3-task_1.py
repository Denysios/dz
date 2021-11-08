def func_division(a, b):
    """Функция деления чисел, с обработкой исключения деления на ноль."""
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        print('На ноль делить нельзя')


user_num1 = int(input('Введите первое число: '))
user_num2 = int(input('Введите второе число: '))
result_div = func_division(user_num1, user_num2)
print(result_div)

# def func_division(a, b):
#     """Функция деления чисел, с проверкой деления на ноль."""
#     assert b != 0
#     c = a / b
#     return c
#
#
# user_num1 = int(input('Введите первое число: '))
# user_num2 = int(input('Введите второе число: '))
# result_div = func_division(user_num1, user_num2)
#
# print(result_div)
