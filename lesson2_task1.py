# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

lst = [100, 'sto', 100.1, True, None, (100, 101), [1, 2, 3], {100: 'sto'}, {100, 'sto'}, range(0, 100)]
for i in lst:
    print(type(i))
