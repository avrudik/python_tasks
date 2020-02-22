import json

men = []
women = []

with open('datafile.json', 'r') as f:
	file = json.load(f)
	for dictionary in file:
		if dictionary['gender'] == 'male':
			men.append(dictionary['name'])
		else:
			women.append(dictionary['name'])

print(f'There are {len(men)} men, whereas the number of women is {len(women)}.')
