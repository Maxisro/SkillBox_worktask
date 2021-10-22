# scores = [8, 5, 10, 7, 6]
# print(scores)
#
# scores[1] *= 3
#
# print(scores)

# monsters_count = int(input('Количество монстров: '))
# mage_index = int(input('Номер мага в списке: '))
# monsters_damage = []
#
# for monster in range(monsters_count):
#     print('Урон у', monster + 1,  ' монстра: ', end='')
#     damage = int(input())
#     monsters_damage.append(damage)
#
# for i_monster in range(monsters_count):
#     if monsters_damage[i_monster] < 100 and i_monster != mage_index - 1:
#         monsters_damage[i_monster] += monsters_damage[mage_index - 1]
#
# print(monsters_damage)

# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
#
# maximum = nums_list[0]
#
#
# for i in range(N):
#     for n in nums_list:
#         if maximum < nums_list[i]:
#             maximum = nums_list[i]
#
# minimum = maximum
# for i in range(N):
#     for n in nums_list:
#         if minimum > nums_list[i]:
#             minimum = nums_list[i]
#
#
# print('Максимальное число в списке:', maximum)
# print('Минимальное число в списке:', minimum)

# summ = 0
# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
# res_list = []
# index_list = []
#
# for i in range(N):
#     print('Введите', i + 1, 'число: ', end='')
#     num = int(input())
#     nums_list.append(num)
#
# divider = int(input('\nВведите делитель: '))
# print()
#
# for i in range(N):
#     if nums_list[i] % divider == 0:
#         res_list.append(nums_list[i])
#         index_list.append(i)
#         summ += i
# for n in range(len(res_list)):
#     print('Индекс числа', res_list[n], ':', index_list[n])
# print('Сумма индексов:', summ)

points = [10, 15, 7, 35, 28, 3]
maximum = points[0]
minimum = points[0]

for i in range(len(points)):
    for n in points:
        if maximum < points[i]:
            maximum = points[i]
            max_index = i
        if minimum > points[i]:
                minimum = points[i]
                min_index = i

print(points)
print('Максимальное число в списке:', maximum, 'index:', max_index)
print('Минимальное число в списке:', minimum, 'index:', min_index)

points[max_index], points[min_index] = points[min_index], points[max_index]

print(points)
