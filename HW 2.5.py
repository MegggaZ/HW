my_list = [8, 6, 5, 5, 3, 3, 2, 2, 1, 1, 1]
user_num = int(input('Введите число: '))
for i, num in enumerate(my_list):
    if int(user_num) < int(num):
        continue
    my_list.insert(i, user_num)
    break
else:
    my_list.append(user_num)
print(my_list)