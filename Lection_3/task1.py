# Нам не известно слово из 5 букв. Каждый раз программа спрашивает пользователя ввести одну букву.
# Если буква в слове есть, то сообщаем об этом, если нет - снимаем попытку с пользователя. Всего попыток 5.
# Если все попытки исчерпаны - игра окончена. 

word = str(input('Введите слово: '))

word_len = len(word)
field = ['*'] * word_len
tries = 5

while tries > 0 and '*' in field:
    letter = input('Крутите барабан: ')
    matched = False

    if len(letter) > 1:
        print('Букву назовете? ')
        continue

    for key in range(word_len):
        if word[key] == letter:
            field[key] = word[key]
            matched = True

    if not matched:
        print('НЕВЕРНО')
        tries -= 1
        print('', tries, '')
    else:
        print('ОТКРОЙТЕ БУКВУ...', letter)

    print(field)

if '*' not in field:
    print('ПРИЗЫ В СТУДИЮ!')
else:
    print('БАНКРОТ')

