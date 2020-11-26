num = [300, 2, 12, 44, 1, 1, 4, 10, 7, 78, 123, 55]
new_list = [number for i, number in enumerate(num) if num[i] > num[i - 1]]

print(new_list)
