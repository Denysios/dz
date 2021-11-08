import random


def my_func(arg1, arg2, arg3):
    """
    Функция принимает на вход 3 аргумента, создает список и присваивает значения,
    затем возвращает сумму двух первых элементов отсортированного списка методом .sort(reverse=True).
    """
    temp_lst = [arg1, arg2, arg3]
    temp_lst.sort(reverse=True)
    return temp_lst[0] + temp_lst[1]


rand_num = []
for i in range(0, 3):
    rand_num.append(round(random.randint(0, 100)))

result = my_func(rand_num[0], rand_num[1], rand_num[2])
print(result)
