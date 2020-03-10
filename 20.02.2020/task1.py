import json

with open('info.txt', 'r') as f:
    file = json.load(f)

    max_money = 0
    
    for dictionary in file:
        if dictionary['amount'] > max_money:
            max_money = dictionary['amount']

    for dictionary in file:
        if dictionary['amount'] == max_money:
            print(dictionary['name'])
