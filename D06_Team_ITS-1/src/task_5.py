import json
import os

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

else:
    print('There is no such patient!')
