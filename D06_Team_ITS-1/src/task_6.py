from tabulate import tabulate
import csv


with open('src/schedule.csv', encoding='utf-8', newline='') as file:
    x = list(csv.reader(file, delimiter=','))
    print(tabulate(x, headers='firstrow', tablefmt='github'))