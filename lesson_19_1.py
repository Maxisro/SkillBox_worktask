# phonebook_list = [
#     ['Ваня', 88006663636],
#     ['Петя', 88005553535],
#     ['Лена', 88007773737]
# ]
# phonebook_dict = {
#     'Ваня': 88006663636,
#     'Петя': 88005553535,
#     'Лена': 88007773737
# }
# name = input('Input Name: ')
#
# if name in phonebook_dict:
#     print(phonebook_dict[name])
# else:
#     print('Ошибка: человек с именем {} не найден.'.format(name))

# student_str = input(
#     'Введите информацию о студенте через пробел\n'
#     '(имя, фамилия, город, место учебы, оценки):'
# )
# student_info = student_str.split()
# student = dict()
# student['Имя'] = student_info[0]
# student['Фамилия'] = student_info[1]
# student['Город'] = student_info[2]
# student['Место учебы'] = student_info[3]
# student['Оценки'] = []
# for i_grade in student_info[4:]:
#     student['Оценки'].append(int(i_grade))
# for i_info in student:
#     print(i_info, '-', student[i_info])

# number = int(input('Введите целое число: '))
# number_dict = dict()
# for i in range(1, number+1):
#     number_dict[i] = i ** 2
# print(number_dict)

phone_book = dict()
flag = True
while flag == True:
    print('Текущие контакты на телефоне:')
    for i_cont in phone_book:
        print(i_cont, phone_book[i_cont])
    name = input('\nВведите имя: ')
    if name in phone_book:
        print('Ошибка: такое имя уже существует.')
        print()
    elif name == 'конец':
        flag = False
    else:
        phone_number = int(input('Введите номер телефона: '))
        phone_book[name] = phone_number
    print()


