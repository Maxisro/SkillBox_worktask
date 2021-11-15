# def ask_user(question,
#              complaint='Неверный ввод. Пожалуйста, введите да или нет',
#              retries=4):
#     while True:
#         answer = input(question).lower()
#         if answer == 'да':
#             return 1
#         if answer == 'нет':
#             return 0
#         retries -= 1
#         if retries == 0:
#             print('Количество попыток истекло.')
#             break
#         print(complaint)
#         print('Осталось попыток:', retries)
#
#
# ask_user('Вы действительно хотите выйти? ')
# ask_user('Удалить файл? ')
# ask_user('Записать файл? ')


def add_lst(num, lst=None):
    lst = list()
    lst.append(num)
    print(lst)


add_lst(5)
add_lst(10)
add_lst(15)