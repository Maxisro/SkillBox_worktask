import os


# speakers_file = open('speakers.txt','r', encoding='utf-8')
# sym_count = []
# for i_line in speakers_file:
#     print(i_line, end='')
#     sym_count.append(str(len(i_line)))
#
# sym_count_str = '\n'.join(sym_count)
# speakers_file.close()
#
# counts_file = open('sym_count.txt', 'w')
# counts_file.write(sym_count_str)
# counts_file.close()

# def find_file(cur_path, file_name):
#     print('переходим', cur_path)
#
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print('     смотрим', path)
#         if file_name == i_elem:
#             return path
#         if os.path.isdir(path):
#            print('это директория')
#            result = find_file(path, file_name)
#            if result:
#                break
#     else:
#         result = None
#
#     return result
#
# file_path = find_file(os.path.abspath
#                       (os.path.join('..', 'SkillBox')),
#                       'lesson_22_3.py'
#                       )
# history_file = open('search_history.txt', 'a')
#
# if file_path:
#     print('Абсолютный путь к файлу:', file_path)
#     history_file.write('\n'+file_path)
# else:
#     print('Файл не найден')
# history_file.close()

cur_path = os.path.abspath(os.path.join('..', 'Python_Basic','Module21'))
for root, dirs, files in os.walk(cur_path):
    for filename in files:
        if filename == 'main.py':
            f_path = os.path.abspath(os.path.join('..', 'Python_Basic','Module21', filename))
            script_text = open(f_path, 'r', encoding='utf-8')
            script_file = open('scripts.txt', 'w')
            script_file.write(str(script_text.read()))
script_text.close()
script_file.close()

