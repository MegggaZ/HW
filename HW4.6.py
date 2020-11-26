from itertools import count, cycle
from functools import reduce

num_start = int(input('Enter numbers start: '))
num_finish = int(input('Enter numbers finish: '))

for i in range(num_start, num_finish):
    print(i)

stop_list = int(input('How many times to repeat?'))
my_list = [1, 2, 3]
a = 0

for i in cycle(my_list):
    a += 1
    if a == stop_list:
        break
    print(i)

