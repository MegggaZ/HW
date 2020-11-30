class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * star for _ in range(self.nums // star)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Sum of all cells ' + str(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'The number of cells cannot be negativeѕ'

    def __mul__(self, other):
        return 'The reproduction of cells is ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Division of cells is ' + str(round(self.nums / other.nums))


cell_1 = Cell(12)
cell_2 = Cell(55)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2.make_order(10))
