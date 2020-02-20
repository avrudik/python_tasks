import csv
import openpyxl


with open('Титаник.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = [row for row in reader]
    book = openpyxl.Workbook()
    sheet = book.active

    survivors = [data[0]]
    sheet.append(data[0])

    for rows, person in data, survivors:
        if rows[0] == '1' and person[1] == 'female':
            survivors.append(rows)
            sheet.append(rows)



    # for row in sheet.iter_rows(min_row=1, max_row=len(survivors)):
    #     for cell, person in row, survivors:
    #         if survivors[person[1]] == 'female':
    #             sheet[cell] = person

    book.save('female_survivors.xlsx')

