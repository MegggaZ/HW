from functools import reduce

num = (i for i in range(100, 1001))
num_sum = reduce(lambda x, y: x + y, num)

print(num_sum)

