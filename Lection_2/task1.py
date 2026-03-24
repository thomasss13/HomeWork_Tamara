# todo: Определить в коде переменные:
# 1. Целочисленного типа
# 2. Вещественного типа
# 3. Логического типа
# 4. Строкового типа
# 5. Пустого типа
# Вывести их типы.

integer_var = 42
float_var = 3.14
bool_var = True
string_var = "Hello, Python!"
none_var = None

print("Значения переменных:")
print(f"Целочисленная: {integer_var}")
print(f"Вещественная: {float_var}")
print(f"Логическая: {bool_var}")
print(f"Строковая: {string_var}")
print(f"Пустая: {none_var}")

print()

print("Типы переменных:")
print(f"Тип целочисленной: {type(integer_var)}")
print(f"Тип вещественной: {type(float_var)}")
print(f"Тип логической: {type(bool_var)}")
print(f"Тип строковой: {type(string_var)}")
print(f"Тип пустой: {type(none_var)}")