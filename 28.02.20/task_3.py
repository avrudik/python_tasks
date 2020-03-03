# Сохранить всю информацию о людях мужского пола в Excel-файле.

from library import *


men = [['name', 'gender', 'amount', 'input_date']]
for filename in list_of_files:
    data = get_data(filename, directory)

    for i in data:
        if type(i) == dict:
            if i['gender'] == 'male':
                i = [i[keys] for keys in i.keys()]
                men.append(i)

        else:
            if type(i) == list:
                if i[1] == 'male':
                    men.append(i)

book = openpyxl.Workbook()
sheet = book.active
for i in men:
    sheet.append(i)

book.save('list_of_men.xlsx')
