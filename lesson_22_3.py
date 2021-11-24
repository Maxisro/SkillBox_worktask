import os


# speakers_file = open('speakers.txt','r')
# m = 'ssas'
# # speakers_file.write(m)
# # data = speakers_file.read()
# # print(data)
#
# for i_line in speakers_file:
#     print(i_line, end='')
#
# speakers_file.close()
path_1 = os.path.abspath(os.path.join('..', '..', '..', 'task', 'group_1.txt'))
path_2 = os.path.abspath(os.path.join('..', '..', '..', 'task', 'Additional_info', 'group_2.txt'))
print(path_1)
print(path_2 + '\n')

file_1 = open(path_1, 'r')
summa = 0
diff = 0
for i_line in file_1:
    info = i_line.split()
    summa += int(info[2])
    diff -= int(info[2])
file_1.close()

file_2 = open(path_2, 'r')
compose = 1
for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])

file_2.close()


print(summa)
print(diff)
print(compose)