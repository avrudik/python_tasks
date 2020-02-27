import json
import openpyxl
import os

# TODO Переписать все функции
def find_files(dir):
    json_files = []
    xl_files = []
    for i in os.listdir(dir):
        if i.endswith('.xlsx') and '~' not in i:
            xl_files.append(i)
        elif i.endswith('.json') and '~' not in i:
            json_files.append(i)
    return [json_files, xl_files] # Возвращает список из двух списков (json и exel файлы)


def get_json(f):
    return json.dump(f)


def get_xl(f):
    return openpyxl.load_workbook(f)


def get_data(dir, file):
    if file in find_files(dir)[0]:
        return get_json(file)
    elif file in find_files(dir)[1]:
        return get_xl(file)
