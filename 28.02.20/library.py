import json
import openpyxl
import os


def find_files(directory_path):
    json_files = []
    xl_files = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.xlsx') and filename.startswith('File') and '~' not in filename:
            xl_files.append(filename)
        elif filename.endswith('.json') and filename.startswith('File') and '~' not in filename:
            json_files.append(filename)
    return [json_files, xl_files]


def get_json_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


def get_xl(filepath):
    book = openpyxl.load_workbook(filepath)
    sheet = book.sheetnames[0]
    whole_file_rows = [rows for rows in book[sheet]]

    data = []
    for rows, i in zip(whole_file_rows, range(len(whole_file_rows))):
        data.append([])
        for cells in rows:
            data[i].append(cells.value)

    return data


def get_data(filepath, directory_):
    if filepath in find_files(directory_)[0]:
        return get_json_data(filepath)
    elif filepath in find_files(directory_)[1]:
        return get_xl(filepath)


list_of_files = [files for files in find_files(os.curdir)[0] + find_files(os.curdir)[1]]
directory = os.curdir

if __name__ == '__main__':
    pass
