# Пользователь вводит строку. Определить число слов в строке, которые начинаются с гласной буквы.

line = input('Введите строку: ').split(' ')
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
count = 0

for word in line:
    for letter in vowels:
        if word[0] == letter:
            count += 1

print(f'Ответ: количество слов в данной строке, начинающихся на гласную букву равно {count}.')
