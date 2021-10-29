# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()

user_lst = input('Введите элементы списка через запятую: ')
user_lst = user_lst.split(',')

# Запрос каждого элемента отдельно
# user_lst = []
# while True:
#     var = input('Введите новый элемент списка, или введите "quit", чтобы закончить ввод: ')
#     if var == "quit":
#         break
#     else:
#         user_lst.append(var)

result_lst = []
i = len(user_lst) // 2
n1 = 0
n2 = 2
cut = []

while i > 0:
    cut = user_lst[n1:n2]
    cut.reverse()
    result_lst.extend(cut)
    n1 += 2
    n2 += 2
    i -= 1

if len(user_lst) % 2 != 0:
    result_lst.append(user_lst[-1])

print(result_lst)
