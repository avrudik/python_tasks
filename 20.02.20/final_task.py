import csv
import openpyxl


with open('titanic.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = [row for row in reader]
    book = openpyxl.Workbook()
    sheet = book.active

    survivors = (data[0])

    for rows in data:
        if rows != data[0]:
            survivors.append(rows)

    for rows in survivors:
        if rows[0] == '1' and rows[1] == 'female':
            survivors.append(rows)
            sheet.append(rows)

    book.save('female_survivors.xlsx')

