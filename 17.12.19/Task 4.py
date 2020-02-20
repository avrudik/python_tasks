# Пользователь вводит число, определить сумму цифр числа.

num = input('Введите число: ')
num_list = num
sum_of_digits = 0

for a in num_list:
    sum_of_digits += int(a)

print(f'Сумма цифр числа {num} составляет {sum_of_digits}')
