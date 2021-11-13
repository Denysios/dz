class Matrix:

    def __init__(self, lst: list):
        self.lst = lst
        print(lst)

    def __str__(self):
        return str(self)

    def __add__(self, other):
        result = []
        for i in range(len(self.lst)):
            result.append(str([(other.lst[i][j] + self.lst[i][j]) for j in range(len(other.lst))]))
        return '\n'.join([i for i in result])


mtrx1 = [[34, 12, 33], [24, 35, 53], [12, 32, 27]]
mtrx2 = [[21, 28, 47], [16, 24, 23], [54, 74, 25]]
mtrx_obj1 = Matrix(mtrx1)
mtrx_obj2 = Matrix(mtrx2)
print(mtrx_obj1 + mtrx_obj2)


# class Matrix:
#
#     def __init__(self, lst: list):
#         self.lst = lst
#
#     def __str__(self):
#         return '\n'.join(map(str, self.lst))
#
#     def __add__(self, other):
#         result = []
#         for i in range(len(self.lst)):
#             result.append([])
#             for x in range(len(self.lst[0])):
#                 result[i].append(self.lst[i][x] + other.lst[i][x])
#         return '\n'.join(map(str, result))
#
#
# m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# mtrx1 = Matrix(m1)
# mtrx2 = Matrix(m2)
# print(mtrx1 + mtrx2)
