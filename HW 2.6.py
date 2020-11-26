base = []
scu = {'название': '', 'цена': '', 'количество': '', 'ед. измерения': ''}
analitic = {'название': [], 'цена': [], 'количество': [], 'ед. измерения': []}
num = 0
while True:
    if input('Для выхода нажмите - q, \nДля продолжения любую клавишу и Enter').lower() == 'q':
        break
    num += 1
    for f in scu.keys():
        user_data = input(f'{f}: ')
        scu[f] = int(user_data) if (f == 'цена' or f == 'колличество') else user_data
        analitic[f].append(scu[f])
    base.append((num, scu.copy()))
    print('Аналитика: ')
    for key, value in analitic.items():
        print(key, value)
