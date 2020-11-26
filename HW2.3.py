user_mounth = int(input('Введите номер месяца: '))
year = ['1', 'Winter', 'Winter',
        'Spring', 'Spring', 'Spring',
        'Summer', 'Summer', 'Summer',
        'Autumn', 'Autumn', 'Autumn', 'Winter']
print(year[user_mounth])

while True:
    try:
        user_mounth = int(input('Введите номер месяца: '))
    except ValueError:
        print('Введено не число!')
        continue
    if user_mounth <= 12 and user_mounth >0:
        break
    else:
        print('Такого месяца не существует!')

year = {1: 'Winter', 2: 'Winter',
        3: 'Spring', 4: 'Spring', 5: 'Spring',
        6: 'Summer', 7: 'Summer', 8: 'Summer',
        9:'Autumn', 10: 'Autumn', 11: 'Autumn',
        12: 'Winter'}
print(year[user_mounth])
