sub_dict = dict()
with open('5.6.txt', encoding='utf-8') as school:
    subject = school.readlines()
    for i in subject:
        all_sub = i.split()
        all_sub_list = all_sub[0]
        each_sub = sum([int(x[:x.find('(')]) for x in all_sub[1:] if '(' in x])
        sub_dict[all_sub_list[::]] = each_sub
print(sub_dict)

