import os


name = input('Enter the full name of patient separated by a space (Ivanov Ivan Ivanovich): ').title()
name = name.replace(' ', '_')

# Такой пациент существует?
if os.path.isdir(f'src/patients/{name}'):
    # Есть ли у него папка visits?
    if os.path.isdir(f'src/patients/{name}/visits'):
        print('Previous doctor appointments:')
        for i in os.listdir(f'src/patients/{name}/visits'):
            print(i[:-4])

        date = input('Enter the date of the appointment you want to watch: ')
        if os.path.isfile(f'src/patients/{name}/visits/{date}.txt'):
            with open(f'src/patients/{name}/visits/{date}.txt', encoding='utf-8') as file:
                print(file.read())
        else:
            print('There was no such appointment with the doctor!')
    else:
        print('This is the first appointment with the doctor!')
else:
    print('There is no such patient!')
