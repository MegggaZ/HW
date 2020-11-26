with open('5.2.txt') as num:
    x = num.readlines()
    print(len(x))

with open('5.2.txt') as num:
    x = num.readlines()
    x_len = len(x)
    i = 1
    num.seek(0)
    while i <= x_len:
        i += 1
        str_len = num.readline().split()
        print(len(str_len))
