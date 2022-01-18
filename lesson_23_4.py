# sym_sum = 0
# line_count = 0
# try:
#     people_file = open('people.txt', 'r')
#     for i_line in people_file:
#         lenght = len(i_line)
#         line_count += 1
#         if i_line.endswith('\n'):
#             lenght -= 1
#         if lenght < 3:
#             raise BaseException('Длина {} строки меньше 3-х символов'.format(line_count))
#         sym_sum += lenght
#     people_file.close()
#
# except FileNotFoundError:
#     print('Файл не найден.')
# finally:
#     print('Найденная сумма символов:', sym_sum)


names_list = []

while True:
    try:
        name = input('Ваше имя: ')
        if name.lower() == 'error':
            raise BaseException('Ты сломал программу!')
        if not name.isalpha():
            raise TypeError
        names_list.append(name)
        if len(names_list) == 5:
            print('Место закончилось')
            break
    except TypeError:
        print('Ты чего ввел?')
    except BaseException:
        names_list = []
        print('Введено стоп-слово.')
        raise ValueError('Пожалуйста, не вводите стоп-слово')


names_file = open('names.txt', 'w')
names_file.write('\n'.join(names_list))
names_file.close()
print('Программа закончена, запись завершена')