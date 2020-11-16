def my_func(a, b, c):
    user_num = [a, b, c]
    user_num.pop(user_num.index(min(user_num)))
    return sum(user_num)


print(my_func(1, 2 , 3))
