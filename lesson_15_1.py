# books_ID = [50, 34, -1, -1, 2, 23, -1]
# new_books_ID = []
# returned = 0
#
# for _ in range(10):
#     id = int(input('Введите ID книги: '))
#     books_ID.append(id)
#
# for id in books_ID:
#     if id == -1:
#         returned += 1
#     else:
#         new_books_ID.append(id)
#
# print('Новый список выданных книг:', new_books_ID)
# print('Вернули за день', returned)

# numbers = [3,7,5]
#
# while True:
#     number = int(input('Новое число: '))
#     numbers.append(number)
#     print('Текущий список чисел:', numbers)
#     for i in numbers:
#         print(i ** 2, i ** 3, i ** 4)
#
# print()

# numbers = []
# for i in range(101):
#     numbers.append(i)
# print(numbers)

count  = int(input('Кол-во сотрудников в офисе: '))
list_ID = []
search = 0

for _ in range(count):
    ID_person = int(input('ID сотрудника: '))
    list_ID.append(ID_person)

ID_search = int(input('Какой ID ищем? '))

for id in list_ID:
    if ID_search == id:
        search += 1


if search == 1:
    print('Сотрудник на месте')
else:
    print('Сотрудник не работает')