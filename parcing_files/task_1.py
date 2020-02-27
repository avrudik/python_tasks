# Найти человека (людей) с самым большим значением в поле amount.

from lib import *

with open('File3.json', 'r') as f:
    dir = os.getcwd()
    file = get_data(dir, f)
    print(file)
