from math import factorial
from itertools import count


def fact():
    for el in count(1):
        yield factorial(el)


num = int(input('Entter number: '))
x = 1
for i in fact():
    print('Factorial {} - {}'. format(x, i))
    if x == num:
        break
    x += 1
