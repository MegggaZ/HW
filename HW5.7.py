import json

firm_dict = dict()
average_profit = []
with open('5.7.txt', encoding='utf-8') as firm:
    firm_r = firm.readlines()
    for i in firm_r:
        name, ooo, revenue, cost = i.split()
        profit = int(revenue) - int(cost)
        firm_dict[name] = profit
        average_profit.append(profit)

average_profit = round(sum(average_profit) / len(average_profit), 2)
all = [firm_dict, {'average_profit': average_profit}]

print(all)

with open('5.7.1.json', 'w', encoding='utf-8') as firm_json:
    json.dump(all, firm_json)

with open('5.7.1.json', encoding='utf-8') as firm_json:
    print(json.load(firm_json))