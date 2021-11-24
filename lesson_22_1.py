import os

#
#
# folder_name = 'project'
# file_name = 'my_file.txt'
#
# path = 'docs/{folder}/{file}'.format(
#     folder=folder_name,
#     file=file_name
# )
#
# print(path)
#
# rel_path = os.path.join('docs', folder_name, file_name)
#
# print(rel_path)
# abs_path = os.path.abspath(file_name)
# print(abs_path)


# def print_dirs(project):
#     print('\nСодержимое директории', project)
#     for i_elem in os.listdir(project):
#         path = os.path.join(project, i_elem)
#         print('     ', path)
#
# projects_list = ['SkillBox', 'Python_Basic']
# for i_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join( '..', i_project))
#     print_dirs(path_to_project)

folder_name = 'access'
file_name = 'admin.bat'

abs_path = os.path.abspath(os.path.join(folder_name, file_name))
print(abs_path)

rel_path = os.path.join('os.getcwd()', folder_name, file_name)
print(rel_path)
print(os.path.abspath(os.sep))
# for dirpath, dirnames, filenames in os.walk("."):
#     # перебрать каталоги
#     for dirname in dirnames:
#         print("Каталог:", os.path.join(dirpath, dirname))
#     # перебрать файлы
#     for filename in filenames:
#         print("Файл:", os.path.join(dirpath, filename))
print(os.getcwd())