# Вывести наибольшую строку.

first_str = input('Введите первую строку: ')
second_str = input('Введите вторую строку: ')

print(f'Размер первой строки равен {len(first_str)}, размер второй - {len(second_str)}.')
num_of_symbols_1 = 0
num_of_symbols_2 = 0

for i in first_str:
    if i != ' ':
        num_of_symbols_1 += 1

for i in second_str:
    if i != ' ':
        num_of_symbols_2 += 1

if num_of_symbols_1 > num_of_symbols_2:
    bigger = 1
else:
    bigger = 2

print(f'Наибольшее количество символов имеет строка №{bigger}.')
print(f'Наибольшая строка - "', end='')
if len(first_str) > len(second_str):
    print(first_str, '".', sep='')
else:
    print(second_str, '".', sep='')
