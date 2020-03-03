# Определить людей с одинаковыми именами (first_name), сохранить информацию в JSON формате.

from task_3 import *

women = []
men = []
for filename in list_of_files:
    data = get_data(filename, directory)

    for i in data:
        if type(i) == dict:
            if i['gender'] == 'female':
                women.append(i['name'])
            if i['gender'] == 'male':
                men.append(i['name'])

        else:
            if type(i) == list:
                if i[1] == 'female':
                    women.append(i[0])
                if i[1] == 'male':
                    men.append(i[0])

same_names = []
for i in men:
    count = 0
    for k in men:
        if i == k or i.split(' ').reverse() == k.split(' '):
            count += 1
    same_names.append({'name': i, 'number_of_coincidences': count})

for i in women:
    count = 0
    for k in women:
        if i == k or i.split(' ').reverse() == k.split(' '):
            count += 1
    same_names.append({'name': i, 'number_of_coincidences': count})

for dictionary in same_names:
    for i in dictionary:
        if type(dictionary[i]) != str and dictionary[i] > 1:
            print(f'{i} has {dictionary[i]} coincidences!')

with open('same_names.json', 'w', encoding="utf-8") as f:
    json.dump(same_names, f, ensure_ascii=False, indent=4)
