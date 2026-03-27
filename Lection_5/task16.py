# todo: База данных пользователя.
# # Задан массив объектов пользователя


# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

# #Затем сообщение для ввода
# Ввидите критерии поиска: 16

# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

print('Выберите тип сортировки: 1 - по возрасту, 2 - по алфавиту, 3 - по уровню доступа')
print('1 - По возрасту')
print('2 - По первой букве')
print('3 - По уровню доступа')

sort_type = input('Тип сортировки: ')
crit = input('Введите критерий поиска: ')
filtered = []

match sort_type:
    case '1':
        try:
            age_crit = int(crit)
            for user in users:
                if user['age'] > age_crit:
                    filtered.append(user)
        except ValueError:
            print('Некорректный критерий поиска')
            filtered = None
            
    case '2':
        letter_crit = str(crit)
        for user in users:
            if user['login'][0].upper() == letter_crit.upper():
                filtered.append(user)
                
    case '3':
        level = str(crit)
        for user in users:
            if user['group'] == level:
                filtered.append(user)
                
    case _:
        print('Сортировка такого типа отсутствует')
        filtered = None

if filtered is not None:
    if filtered:
        print('Результат:')
        for user in filtered:
            print(f"Пользователь: '{user['login']}' возраст {user['age']} года, группа \"{user['group']}\"")
    else:
        print('Не найдено')