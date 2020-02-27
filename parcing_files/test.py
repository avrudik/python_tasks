from lib import *

file = os.getcwd() + '\File1.xlsx'
book = openpyxl.load_workbook(file)
sheet = book.get_sheet_names()[0]
rows = [rows for rows in book[sheet]]


for i in rows:
    for cells in i:
        print(cells.value)
