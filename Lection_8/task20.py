#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

# выходные данные:
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

file_input = open("input.txt", "rt", encoding = "utf-8")
file_output = open("output.txt", "wt", encoding = "utf-8")

lines = file_input.readlines()

for line in lines[::-1]:
    file_output.writelines(line)

file_input.close()
file_output.close()