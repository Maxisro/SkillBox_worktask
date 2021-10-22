# data = dict()
# # что-то происходит
# print(data.get('server'))
# data['server'] = {
#     'host': '127.0.0.1',
#     'port': '10'
# }
# # что-то происходит
# if data.get('configuration', {}).get('ssh', {}).get('login', {}):
#     print('В структуре уже есть логин')
# data['configuration'] = {
#     'ssh': {
#         'access': 'true',
#         'login': 'Ivan',
#         'password': 'qwerty'
#     }
# }
# print(data)
# print(data['server']['port'])
# data['configuration']['ssh']['login'] = 'VOVA'
# print(data)
# print()
# for i_value in data.values():
#     for j_key in i_value:
#         print(j_key, i_value[j_key])

# players_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
# team_a_members = [
#     player['name']
#     for player in players_dict.values()
#     if player['team'] == 'A' and player['status'] == 'Rest'
# ]
# team_b_members = [
#     player['name']
#     for player in players_dict.values()
#     if player['team'] == 'B' and player['status'] == 'Training'
# ]
# team_c_members = [
#     player['name']
#     for player in players_dict.values()
#     if player['team'] == 'C' and player['status'] == 'Travel'
# ]
#
# print('Все члены команды из команды А, которые отдыхают.', team_a_members)
# print('Все члены команды из группы B, которые тренируются.', team_b_members)
# print('Все члены команды из команды C, которые путешествуют.', team_c_members)

family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children":[
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

chil = family_member.get('children')
for i in chil:
    ch = dict(i)
    if ch.get('name',{}) == 'Bob':
        childe_name = ch.get('name',{})
        print(childe_name)
        break
        print('Нет такого')
family = family_member.get('surname', {})

print(family)