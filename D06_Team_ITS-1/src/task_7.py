from tabulate import tabulate
import csv


name = input('Enter the full name of patient separated by a space (Ivanov Ivan Ivanovich): ').title()

with open('src/schedule.csv', encoding='utf-8', newline='') as file:
    x = list(csv.reader(file, delimiter=','))
k = 0
for i in range(len(x)):
    if name in x[i]:
        x[i][2] = 'Yes'
        k += 1

if k == 0:
    print('There is no such patient!')
else:
    with open('src/schedule.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(x)
        print(tabulate(x, headers='firstrow', tablefmt='github'))
