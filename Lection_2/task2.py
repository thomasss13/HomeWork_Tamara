# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
#
# Преобразуйте переменную age в Boolean
# age = "123abc"
#
# Преобразуйте переменную flag в Boolean
# flag = 1
#
# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
#
# Преобразуйте значение 0 и 1 в Boolean
#
# Преобразуйте False в строку

age = '23'
print(int(age))

foo = '23abc'
try:
    print(int(foo))
except:
    print('ValueError')

age = '123abc'

try:
    print(bool(age))
except:
    print('ValueError')

flag = 1
print(bool(flag))

str_one = 'Privet'
try:
    print(bool(str_one))
except:
    print('ValueError')

str_two = ''
try:
    print(bool(str_two))
except:
    print('ValueError')

zero = 0
print(bool(zero))

one = 1
print(bool(one))

false = False
print(str(false))