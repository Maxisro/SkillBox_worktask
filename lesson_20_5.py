# 1 task
# phonebook_dict = {
#     ('Петров', 'Ваня'): 88006663636,
#     ('Егоров', 'Ваня'): 88003333333,
#     ('Ульянов', 'Петя'): 88005553535,
#     ('Сидорова', 'Лена'): 88007773737
# }
# phonebook_dict[('Сидорова', 'Алена')] = 109090
#
# for i_person in phonebook_dict:
#     if 'Сидорова' in i_person:
#         print(i_person[1], phonebook_dict[i_person])
#
# print(phonebook_dict)

# 2 task
data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

ser_pas = int(input('введите серию паспорта: '))
num_pas = int(input('Введите номер паспорта: '))

for i_pas in data:
    if i_pas[0] == ser_pas and i_pas[1] == num_pas:
        print(*data[i_pas])