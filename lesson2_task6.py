# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.

def product_func(d, b):
    dict_product = {}
    for i in b:
        name = input(f'Введите {i} товара {d}: ')
        temp = (i, name)
        dict_product.update([temp])
    result1 = (d, dict_product)
    return result1


def analysis_func(lst_result, variable):
    n = 0
    lst = []
    # цикл вытягивания значений по ключу
    for element in lst_result:
        val = (lst_result[n][1].get(variable))
        n += 1
        lst.append(val)
    return lst


result = []
list_characteristics = ['наименование', 'цена', 'количество', 'ед_изм']
unit_product = input('Введите колиство товара (число), которое хотите записать: ')
int(unit_product) if unit_product.isdigit() else print(f'Введено неверное значение. Запустите приложение снова.')
x = int(unit_product)
c = 1

while x > 0:
    product = product_func(c, list_characteristics)
    product = tuple(product)
    result.append(product)
    c += 1
    x -= 1

for i in result:
    print(i)

# Часть 2, Анализ
analysis_list = {}

# Хотел реализовать это через генератор списков, но не смог понять как в переменную z записать список циклом и
# как реализовать счетчик индекса кортежей n.. Очень хотелось записать это в пару строк))

# analysis_list = {x: z for x in list_characteristics for z in (result[n][1].get(x))}

for el in list_characteristics:
    analysis = analysis_func(result, el)
    temp_dict = (el, analysis)
    analysis_list.update([temp_dict])

print(f'Значения характеристик товара:\n{analysis_list}')
