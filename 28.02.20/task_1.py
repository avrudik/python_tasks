# Найти человека (людей) с самым большим значением в поле amount.

from library import *

for filename in list_of_files:
    data = get_data(filename, directory)
    max_amount = 0
    name_with_max_amount = 0

    for i in data:
        if type(i) == dict:
            if i['amount'] > max_amount:
                max_amount = i['amount']
                name_with_max_amount = i['name']
        else:
            if type(i) == list:
                if i[2] != 'amount' and int(i[2]) > max_amount:
                    max_amount = i[2]
                    name_with_max_amount = i[0]

    print(name_with_max_amount, '-', max_amount)
