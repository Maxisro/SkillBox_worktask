import os


# def print_dirs(project):
#     print('\nСодержимое директории', project)
#     if os.path.exists(project):
#         for i_elem in os.listdir(project):
#             path = os.path.join(project, i_elem)
#             print('     ', path)
#     else:
#         print('Каталога проекта не существует')
#
#
# projects_list = ['Prod', 'skillbox', 'Python_Basic']
# for i_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join( '..', i_project))
#     print_dirs(path_to_project)


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
#                       'lesson_22_1.py'
#                       )
#
# if file_path:
#     print('Абсолютный путь к файлу:', file_path)
# else:
#     print('Файл не найден')

# path_abs = os.path.abspath('lesson_22_3.py')
path_abs = os.path.dirname(os.path.abspath('lesson_22_3.py'))
size = os.path.getsize(path_abs)

print('Путь:', path_abs)
if os.path.exists(path_abs):
    if os.path.isdir(path_abs):
        print('Это директория')
        print('Размер директории:', size, 'байт')
    else:
        print('Это файл')
        print('Размер файла:', size, 'байт')
else:
    print('Указанного пути не существует')