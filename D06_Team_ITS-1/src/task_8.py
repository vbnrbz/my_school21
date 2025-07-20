import json
import os
import csv
from datetime import datetime


name = input('Enter the full name of patient separated by a space (Ivanov Ivan Ivanovich): ').title()
name = name.replace(' ', '_')

if os.path.isdir(f'src/patients/{name}'):
    if os.path.isfile(f'src/patients/{name}/card.json'):
        with open(f'src/patients/{name}/card.json', encoding='utf-8') as file:
            x = json.load(file)
            print(json.dumps(x, indent=4))
    else:
        print('There is no patient card!')

        surname = input('Enter the surname of patient: ').title()
        firstname = input('Enter the name of patient: ').title()
        patronymic = input('Enter the patronymic of patient: ').title()
        birth = input('Enter the date of birth of patient (1994-01-10): ')
        sex = input('Enter the sex of patient (M or W): ').title()

        d = {}
        d['Surname'] = surname
        d['Name'] = firstname
        d['Patronymic'] = patronymic
        d['Date of birth'] = birth
        d['Sex'] = sex

        with open(f'src/patients/{name}/card.json', 'w', encoding='utf-8') as file:
            json.dump(d, file, indent=4)
            print(json.dumps(d, indent=4))

# после вывода CARD.JSON

    while True:
        quest = input(f'''{'-' * 50}
Enter:
 - 1, if you want to see a list of dates of previous visits;
 - 2, if you want to see the recording of the previous visit;
 - 3, if you want to start recording in the current visit;
 - 4, if you want to finish the appointment and complete the program.
{'-' * 50}    
''')
        # ПЕРВАЯ ОПЦИЯ
        if quest == '1':
            if os.path.isdir(f'src/patients/{name}/visits'):
                print('Previous doctor appointments:')
                for i in os.listdir(f'src/patients/{name}/visits'):
                    print(i[:-4])
            else:
                print('This is the first appointment with the doctor!')

        # ВТОРАЯ ОПЦИЯ
        if quest == '2':
            if os.path.isdir(f'src/patients/{name}/visits'):
                date = input('Enter the date of the appointment you want to watch: ')
                if os.path.isfile(f'src/patients/{name}/visits/{date}.txt'):
                    with open(f'src/patients/{name}/visits/{date}.txt', encoding='utf-8') as file:
                        print(file.read())
                else:
                    print('There was no such appointment with the doctor!')
            else:
                print('This is the first appointment with the doctor!')

        # ТРЕТЬЯ ОПЦИЯ
        if quest == '3':
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

        # ЧЕТВЕРТАЯ ОПЦИЯ
        if quest == '4':
            with open('src/schedule.csv', encoding='utf-8', newline='') as file:
                x = list(csv.reader(file, delimiter=','))
            new_name = name.replace('_', ' ')
            for i in range(len(x)):
                if new_name in x[i]:
                    x[i][2] = 'Yes'

            with open('src/schedule.csv', 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerows(x)
            break

else:
    print('There is no such patient!')
