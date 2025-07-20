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
else:
    print('There is no such patient!')
