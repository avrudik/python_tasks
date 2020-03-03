# Сохранить всю информацию о людях мужского пола в Excel-файле.

from library import *


men = []
for filename in list_of_files:
    data = get_data(filename, directory)

    for i in data:
        if type(i) == dict:
            if i['gender'] == 'male':
                men.append(i['name'])

        else:
            if type(i) == list:
                if i[1] == 'male':
                    men.append(i[0])

book = openpyxl.Workbook()
sheet = book.active
for i in men:
    i = [name for name in i.split(' ')]
    sheet.append(i)

book.save('list_of_men.xlsx')
