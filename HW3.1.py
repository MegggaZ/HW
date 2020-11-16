def fun(x, y):
    try:
        a = user_num1 / user_num2
        print(a)
    except ZeroDivisionError:
        print('Деление на ноль запрещено!')


user_num1 = int(input('Введите первое число: '))
user_num2 = int(input('Введите второе число: '))

print(fun(1, 2))
