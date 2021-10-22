# word= input('Введите слово: ')
# replace_num = int(input('Номер символа на замену: '))
# replace_sym = input('Чем заменяем: ')
# sym_list = list(word)
#
# sym_list[replace_num-1] = replace_sym
# for i in sym_list:
#     print(i, end='')

# words_list = []
# counts = [0, 0, 0]
#
# for i in range(3):
#     print('Введите', i + 1, 'слово: ', end='')
#     word = input()
#     words_list.append(word)
#
# text = input('Слово из текста: ')
# while text != 'end':
#     for index in range(3):
#         if words_list[index] == text:
#             counts[index] += 1
#     text = input('Слово из текста: ')
#
# print('\nПодсчет слов в тексте')
# for i in range(3):
#     print(words_list[i], ':', counts[i])

# text = input('Введите текст: ')
# text_list = list(text)
# count = 0
#
# for t in range(len(text_list)):
#     for i in text_list:
#         if text_list[t] == ':':
#             text_list[t] = ';'
#             count += 1
#
#
# print('Исправленная строка: ', end='')
# for i in text_list:
#     print(i, end='')
# print('\nКол-во замен:', count)