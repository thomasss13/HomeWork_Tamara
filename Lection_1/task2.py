import math

try:
  leg_1 = float(input('Введите длину первого катета ')) 
  leg_2 = float(input('Введите длину второго катета ')) 
except:
  print('Ошибка ввода')
  exit()


hypotenuse_func = float(math.sqrt(leg_1**2 + leg_2**2)) 
hypotenuse_op = float((leg_1**2 + leg_2**2)**0.5)


if leg_1 + leg_2 <= hypotenuse_func or leg_1 + hypotenuse_func <= leg_2 or leg_2 + hypotenuse_func <= leg_1:
  print('Вычислительная ошибка')
  exit()

if leg_1 == 0 or leg_2 == 0 or hypotenuse_func == 0:
  print('Вычислительная ошибка')
  exit()

if hypotenuse_func != hypotenuse_op:
  print('Вычислительная ошибка')
  exit()


print('Получено значение гипотенузы: ', hypotenuse_func)