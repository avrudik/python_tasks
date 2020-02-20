import json

strawberry = []
banana = []
apple = []

with open('datafile.txt', 'r') as f:
    file = json.load(f)
    for dictionaries in file:
        if dictionaries['favoriteFruit'] == 'strawberry':
            strawberry.append(dictionaries['name'])
        elif dictionaries['favoriteFruit'] == 'banana':
            banana.append(dictionaries['name'])
        elif dictionaries['favoriteFruit'] == 'apple':
            apple.append(dictionaries['name'])


print('People, who like strawberries:')
for i in range(len(strawberry)):
    print(str(i+1) + ')', strawberry[i])

print('\n')

print('People, who like apples:')
for i in range(len(apple)):
    print(str(i+1) + ')', apple[i])

print('\n')

print('People, who like bananas:')
for i in range(len(banana)):
    print(str(i+1) + ')', banana[i])
