def func_data(f1='имя', f2='год рождения', f3='город проживания', f4='эл. почта', f5='телефон'):
    """
    Функция принимает именованные аргументы, создает словарь и присваивает их ключам,
    которые берутся из кортежа params
    """
    userdata = {params[0]: f1, params[1]: f2, params[2]: f3, params[3]: f4, params[4]: f5}
    print(userdata)


params = ('имя', 'год рождения', 'город проживания', 'эл. почта', 'телефон')
name = input(f'Введите {params[0]}: ')
birth = input(f'Введите {params[1]}: ')
city = input(f'Введите {params[2]}: ')
email = input(f'Введите {params[3]}: ')
phone = input(f'Введите {params[4]}: ')

func_data(f1=name, f2=birth, f3=city, f4=email, f5=phone)
