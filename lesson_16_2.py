langs = ['Python', 'Java', 'JS', 'SQL']
# new_langs = []
# for i_lang  in range(2):
#     new_langs.append(langs[i_lang])
# new_langs.append('C++')
# for i_lang in range(2, len(langs)):
#     new_langs.append(langs[i_lang])
user_lang = input('После чего вставить? ')
i_lang = langs.index(user_lang)
langs.insert(i_lang + 1, 'C++')

print(langs)
