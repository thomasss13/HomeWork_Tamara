# загадать число от 1 до 100. Игрок вводит числа, пока не угадает число.
# У него есть 5 попыток.

import random

rn = int(random.randint(1, 100))
print(rn)

for i in range(5):
    inp = int(input('Введите число: '))
    if inp < rn:
        print('Больше')
    if inp == rn:
        print('Верно!')
        break
    if inp > rn:
        print('Меньше')
    if i == 5:
        print('Попытки закончились!')
        print('Загаданное слово было: ', rn)
    