def my_func(x, y):
    degree = x ** y
    return degree


print(my_func(2, 3))


def my_func(x, y):
    x, y = float(x), int(y)
    res = x
    for i in range(abs(y) - 1):
        res *= x
    return 1/res


print(my_func(2, -3))
