import csv
import openpyxl

with open('titanic.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = [row for row in reader]

book = openpyxl.Workbook()
sheet = book.active

survivors = [data[0]]

for row in data:
    if row != data[0]:
        if row[0] == '1' and row[1] == 'female':
            survivors.append(row)

for rows, lists in zip(sheet.iter_rows(max_row=len(survivors), max_col=len(survivors[0])), survivors):
    for cell, data in zip(rows, lists):
        cell.value = data
book.save('female_survivors.xlsx')
