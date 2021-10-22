# # 1 task
# score_dict = {
#     'Ваня': 33,
#     'Петя': 60,
#     'Лена': 45
# }
#
# for i_name, i_score in score_dict.items():
#     print(i_name, i_score)

# 2 task
# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
#
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520},
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }
#
# for i_title, i_code in goods.items():
#     total_quantity = 0
#     total_cost = 0
#     for j_good in store[i_code]:
#         total_quantity += j_good['quantity']
#         total_cost += j_good['price'] * j_good['quantity']
#     print('{title} - {quantity} шт, стоимость {cost} руб.'.format(
#        title=i_title,
#        quantity=total_quantity,
#        cost=total_cost
#     ))

# 3 task
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# for i_name, i_cost in incomes.items():
#     print(i_name, i_cost, sep=' -- ')

# 4 task
# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }
# for i_name, i_inf in server_data.items():
#     print(f'{i_name}:')
#     for j_name, j_inf in i_inf.items():
#         print(f'\t{j_name}: {j_inf}')

# 5 task
print([i_val for i_key, i_val in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])
