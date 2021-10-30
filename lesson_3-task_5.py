def sum_numbers():
    """Программа суммирует введенные числа через пробел. Для выхода, нужно ввести 'quit'."""
    result = 0
    while True:
        user_numbers = input('Введите числа через пробел. Для остановки программы введите "quit": ').split(' ')
        for i in user_numbers:
            if i == 'quit':
                return result
            else:
                try:
                    result += int(i)
                except ValueError as error:
                    print('Введено некорректное значение', error)
                    break
        print(result)


print(sum_numbers())
