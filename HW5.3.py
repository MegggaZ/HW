with open('5.3.txt', encoding='utf-8') as state:
    state.seek(0)
    for i in state:
        x = state.readline().split()
        dict_user = {x[0]: x[1]}
    for a in dict_user:
        new_dict = map(float, dict_user.values())
    # if type(dict_user[1]) == str:

        print(type(dict_user.values()))
        print(dict_user)
        print(a)
        # if dict_user[1] <= 20000:
        #     print(dict_user)
