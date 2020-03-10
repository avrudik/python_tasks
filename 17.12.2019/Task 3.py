# а) Создать список из 20 элементов со случайными значениями в диапазоне, введенным пользователем.
# Вывести получившийся список.
# Примечание: для генерации случайных элементов использовать модуль random. Метод randint(a,b), где [a;b]

from random import *

list_of_num = []
range_of_num = input('Введите диапазон чисел (нижнюю и верхнюю границу через пробел): ').split(' ')

for a in range(20):
    list_of_num.append(randint(int(range_of_num[0]), (int(range_of_num[1]) + 1)))
print(list_of_num)

# б)  Определить количество четных и нечетных элементов в полученном списке.
even = 0
odd = 0

for i in list_of_num:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'В данном списке количество четных элементов равно {even}, а нечетных - {odd}.')
