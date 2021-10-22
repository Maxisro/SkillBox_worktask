# 1 task
# scores = [54, 67, 48, 99, 27]
# for i_player, i_score in enumerate(scores):
#     print(i_player, i_score)

# 2 task

# text = str('so~mec~od~e')
# print('Ответ: ', end='')
# for i_index, i_symb in enumerate(text):
#
#     print(i_index if i_symb == '~' else "", end='')

# 3 task
import random
import string


first_list = list(random.choice(string.ascii_letters) for _ in range(10))
second_list = list(random.choice(string.ascii_letters) for _ in range(10))
print(first_list)
print(second_list, '\n')

first_dict = dict((i, v) for i, v in enumerate(first_list))
second_dict = dict((i, v) for i, v in enumerate(second_list))
print(first_dict)
print(second_dict)
