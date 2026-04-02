# todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# – id. Номер по порядку (от 1 до 10); 
# – текст из списка algoritm;

# Каждое значение из списка должно находится на отдельной строке.
# Выход:
# |-----------------|
# | 1 | "C4.5"      |
# | 2 | "k - means" |
# и т.д.

import csv

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

file = open("algoritm.csv", "wt", encoding = "utf-8")

writer = csv.writer(file)
writer.writerow(["id", " algoritm"])

for i in range(len(algoritm)):
    writer.writerow([i + 1, algoritm[i]])

file.close()