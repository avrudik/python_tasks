import json

open('list_of_people.txt', 'w').write('There are people older than 30:\n')

number = 1
with open('datafile.txt', 'r') as f:
	file = json.load(f)
	for dictionary in file:
		if dictionary['age'] > 30:
			with open('list_of_people.txt', 'a') as new_file:
				new_file.write(str(number) + ')' + f' {dictionary["name"]}' + '\n')
			number += 1