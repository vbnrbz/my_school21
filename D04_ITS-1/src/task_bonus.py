from tabulate import tabulate
from random import choice


headers = ['', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
langs = ['Latin', 'English', 'Python', 'Rest']
l = []

for i in range(1, 5):
    a = [i]
    for j in range(7):
        a.append(choice(langs))
    l.append(a)

print(tabulate(l, headers, tablefmt='github'))
