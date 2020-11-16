def sum():
    x = False
    res = 0
    while x == False:
        numbers = list(input('Введите числа, для выхода нажмите q: '))
        res_sum = int(0)
        for i in numbers:
            if 'q' in i:
                x = True
                break
            res_sum += int(i)
        res += res_sum
        print(res)
    return res


sum()
