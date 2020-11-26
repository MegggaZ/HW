with open('5.4.txt', encoding='utf-8') as eng:
    i = eng.readlines()

with open('5.4.1.txt', 'w', encoding='utf-8') as eng:
    for line in i:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        eng.write(line)


