with open('5.5.txt', 'w', encoding='utf-8') as num:
    numbers = input('Enter numbers: ')
    num.write(numbers + '\n')
    my_list = numbers.split()
    a = list(map(int, my_list))
    sum_a = sum(a[::])
    num.write(str(sum_a))
print(sum_a)


