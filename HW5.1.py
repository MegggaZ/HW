with open('5.1.txt', 'w+', encoding='utf-8') as user_str:
    while True:
        user = input('Enter string: ')
        if user == '':
            user_str.seek(0)
            print(user_str.readlines())
            break
        user_str.write(user + '\n')

