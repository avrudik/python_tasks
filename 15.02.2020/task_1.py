import json
with open('datafile.json', 'r') as f:
	file = json.load(f)
	for dictionary in file:
		if dictionary['eyeColor'] == 'blue':
			print(dictionary['name'])
