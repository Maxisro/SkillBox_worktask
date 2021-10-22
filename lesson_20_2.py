# def add_num(seq, number):
#     seq = list(seq)
#     for i_num in range(len(seq)):
#         seq[i_num] += number
#     return seq
#
#
# origin_tuple = (3, 1, 4, 1, 5)
# changed_list = add_num(origin_tuple, 5)
#
# print(origin_tuple)
# print(changed_list)

# import random
#
#
# def create_tuple(start, stop):
#     new_tuple = tuple(random.randint(start, stop) for _ in range(10))
#     return new_tuple
#
#
# first_tuple = create_tuple(0, 5)
# second_tuple = create_tuple(-5, 0)
# third_tuple = first_tuple + second_tuple
#
# print(third_tuple, 'нолей =', third_tuple.count(0))
import math


def square_calculation(r, h):
    '''
    Функция для расчёта площади боковой поверхности цилиндра и его полной площади.
    :param r: радиус
    :param h: высота
    :return: возвращает side - боковую поверхность и full - полную площадь.
    '''
    side = 2 * math.pi * r * h
    s = math.pi * r**2
    full = side + 2 * s
    return round(side,2 ), round(full, 2)


r = int(input('Input radius: '))
h = int(input('Input height: '))

side, full = square_calculation(r, h)

print('\nПлощадь боковой поверхности =', side)
print('Полная площадь =', full)