import json

with open('datafile.json', 'r', encoding='utf-8') as f:
    file = json.load(f)
    fruit = {}

    for dicts in file:
        if dicts['favoriteFruit'] not in fruit:
            fruit[dicts['favoriteFruit']] = []

    for dicts in file:
        if dicts['favoriteFruit'] in fruit:
            kind_of_fruit = dicts['favoriteFruit']
            fruit[kind_of_fruit].append(dicts['name'])

    for fruits in fruit:
        print(f'People, who like {fruits}:')
        for people in fruit[fruits]:
            print(people)
        print('\n')
