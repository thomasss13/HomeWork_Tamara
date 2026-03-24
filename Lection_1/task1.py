try:
    age = int(input('Введите возраст: '))
except:
    print('Ошибка ввода')
    exit()

if age < 18:
    print('Вам еще нет 18')
else:
    print('Вход разрешен')