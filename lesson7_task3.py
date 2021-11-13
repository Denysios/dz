class Cell:

    def __init__(self, param: int):
        self.param = param

    def __str__(self):
        return f'{self.param * "*"}'

    def __add__(self, other):
        return f'Результат сложения: {Cell(self.param + other.param)}'

    def __sub__(self, other):
        res = self.param - other.param
        return f'Результат вычитания: {Cell(res if res > 0 else print(f"Результат отрицателен"))}'

    def __mul__(self, other):
        return f'Результат умножения: {Cell(self.param * other.param)}'

    def __truediv__(self, other):
        return f'Результат деления: {Cell(self.param // other.param)}'

    def make_order(self, rows):
        row = ''
        for i in range(int(self.param // rows)):
            row += f'{"*" * rows} \n'
        row += f'{"*" * (self.param % rows)}'
        print(f'Данные записаны в таблицу клеток ({int(self.param // rows) + 1} * {rows})')
        return row


a = 23
b = 7
numb1 = Cell(a)
numb2 = Cell(b)
print(numb1 + numb2)
print(numb1 - numb2)
print(numb1 * numb2)
print(numb1 / numb2, end='\n\n')
print(numb1.make_order(9), end='\n\n')
print(numb2.make_order(9))
