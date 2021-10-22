# punct = set('.,;:!?')
# text = 'Я! Есть. Грут?! Я, Грут и Есть.'
# count = 0
# for sym in text:
#     if sym in punct:
#         count += 1
# print('Количество знаков пунктуации:', count)
# import random
# nums_1 = set([29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11,
#               2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1])
#
# nums_2 = set([16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9,
#               12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21])
#
# print('1-е множество:', nums_1)
# print('2-е множество:', nums_2)
# print('\nМинимальный элемент 1-го множества:',min(nums_1))
# print('Минимальный элемент 2-го множества:',min(nums_2))
#
# nums_1.remove(min(nums_1))
# nums_2.remove(min(nums_2))
# rand_num1 = random.randint(100,200)
# rand_num2 = random.randint(100,200)
#
# print('\nСлучайное число для 1-го множества:', rand_num1)
# print('Случайное число для 2-го множества:', rand_num2)
#
# nums_1.add(rand_num1)
# nums_2.add(rand_num2)
#
# print('\nОбъединение множеств:', nums_1.union(nums_2))
# print('Пересечение множеств:', nums_1 & nums_2)
# print('Элементы, входящие в nums_2, но не входящие в nums_1: ', nums_2 - nums_1)

text = 'ab1n32kz2'
num = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
text_num = set(text)

print(*text_num & num)
a= set()
for sym in text:
    if '0' <= sym <= '9' and sym not in a:
        a.add(sym)
print(*a)