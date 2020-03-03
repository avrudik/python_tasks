# Сохранить всю информацию о людях, у которых дата в поле input_date больше '12.03.2017' в файл JSON формата.
# (для определение даты используйте библиотеку datetime: ссылка1 и ссылка2)

from library import *
import datetime


def to_date(string):
    date = [int(item) for item in string.split('.')]
    return datetime.date(date[2], date[1], date[0])


date_to_compare = to_date('12.03.2017')
list_of_people = []

for filename in list_of_files:
    data = get_data(filename, directory)

    for i in data:
        if type(i) == dict:
            if to_date(i['input_date']) > date_to_compare:
                list_of_people.append(i['name'])
        else:
            if type(i) == list:
                if i[3] != 'input_date' and to_date(i[3]) > date_to_compare:
                    list_of_people.append(i[0])

with open('Persons_wih_date_greater_than_in_condition.json', 'w', encoding="utf-8") as f:
    json.dump(list_of_people, f, ensure_ascii=False, indent=4)
