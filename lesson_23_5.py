sym_sum = 0
line_count = 0
try:
    with open('people.txt', 'r') as people_file:
       for i_line in people_file:
            lenght = len(i_line)
            line_count += 1
            if i_line.endswith('\n'):
                lenght -= 1
            if lenght < 3:
                raise BaseException('Длина {} строки меньше 3-х символов'.format(line_count))
            sym_sum += lenght

except FileNotFoundError:
    print('Файл не найден.')
finally:
    print('Найденная сумма символов:', sym_sum)
    print(people_file.closed)