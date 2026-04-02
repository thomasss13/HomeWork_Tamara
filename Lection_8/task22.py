#todo: Модифицировать программу таким образом чтобы она выводила
#  приветствие "Hello", которое до этого записано в файл text.txt
#  через метод write()

f = open("text.txt", "w+t", encoding = "utf-8")
f.write("Hello\n")

f.seek(0)
print(f.read())

f.close()
