enter = list(input('Ведите что хотите: '))
for i in range(0, len(enter), 2):
    enter[i - 1], enter[i] = enter[i], enter[i - 1]
print(enter)
