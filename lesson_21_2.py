# def factorial(num):
#     if num == 1:
#         return 1
#     fact_n = factorial(num - 1)
#     return num * fact_n
#
#
# num_fact = factorial(5)
# print(num_fact)


# def find_key(struct, key):
#     if key in struct:
#         return struct[key]
#     for sub_struct in struct.values():
#         if isinstance(sub_struct, dict):
#             result = find_key(sub_struct, key)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
# user_key = input('Какой ключ ищем? ')
# value = find_key(site, user_key)
# if value:
#     print(value)
# else:
#     print('Такого ключа в структуре сайта нет.')

# def power(a, n):
#     if n == 1:
#       return a
#     f_n = power(a, n - 1)
#     return a * f_n
#
#
# float_num = 1.5 #float(input('Введите вещественное число: '))
# int_num = 5 #int(input('Введите степень числа: '))
# print(float_num, '**', int_num, '=', power(float_num, int_num))
