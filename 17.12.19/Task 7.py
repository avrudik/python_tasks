# Пользователь вводит строку без знаков препинания которая состоит из нескольких слов.
# Определить самое длинное слово в строке.
# Примечание: задание на повышенную сложность * рассмотреть случай,
# когда пользователь вводит строку со знаками препинания.

line = input('Введите строку: ').split(' ')
list_of_lengths = []

for a in range(len(line)):
    len_of_word = 0
    for i in line[a]:
        for x in range(21, int('2F', 16) + 1) or range(int('3A', 16), int('3F', 16) + 1):
            if i == chr(x):
                len_of_word -= 1
        len_of_word += 1
    list_of_lengths.append(len_of_word)
print(list_of_lengths)
print(f'Самое длинное слово в данной строке - '
      f'"{line[list_of_lengths.index(max(list_of_lengths), 0, len(list_of_lengths))]}".')

# Хоть в ответе и может напечатать слово со знаком препинания,
# он не учитывается в подсчете количества букв в этом слове.
