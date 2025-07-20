import os
from datetime import datetime


name = input('Enter the full name of patient separated by a space (Ivanov Ivan Ivanovich): ').title()
name = name.replace(' ', '_')

# Такой пациент существует?
if os.path.isdir(f'src/patients/{name}'):
    print('Enter records for the current appointment (to finish press Enter twice):')
    l = list()
    l.append(input())
    k = 0
    if l[0] == '':
        k += 1

    while k < 2:
        l.append(input())
        if l[-1] == '':
            k += 1
        else:
            k = 0

    with open(f'src/patients/{name}/visits/{datetime.today().date()}.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(l[:-1]))

else:
    print('There is no such patient!')
