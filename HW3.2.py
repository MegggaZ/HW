def fun(**kwargs):
    return kwargs


print(fun(
    name=input('Введите имя: '),
    surname=input('Введите фамилию: '),
    year=input('Введите год рождения: '),
    city=input('Введите город проживания: '),
    mail=input('Введите email: '),
    phone=input('Введите телефон: ')
))
