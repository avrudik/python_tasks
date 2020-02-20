import json
with open('datafile.txt', 'r') as f:
	file = json.load(f)
	for dictionary in file:
		if dictionary['eyeColor'] == 'blue':
			print(dictionary['name'])