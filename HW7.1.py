class Matrix:
    def __init__(self, list_m):
        self.list_m = list_m

    def __str__(self):
        return '\n'.join([' '.join([str(i) for i in line]) for line in self.list_m])

    def __add__(self, other):
        matrix_all = ''
        if len(self.list_m) == len(other.list_m):
            for line_1, line_2 in zip(self.list_m, other.list_m):
                if (line_1) != len(line_2):
                    return 'Matrices are not equal'

                sum_line = [x + y for x, y in zip(line_1, line_2)]
                matrix_all += ''.join([str(i) for i in sum_line]) + '\n'

        else:
            return 'Matrices are not equal'
        return matrix_all


m_1 = Matrix([[3, 8], [5, 3], [8, 7], [3, 1]])
m_2 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
print(m_1)
print(m_1 + m_2)
