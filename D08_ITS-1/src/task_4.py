from tabulate import tabulate
from src.utils import add_patient_to_schedule
import csv

def main():
    with open('src/schedule.csv', encoding='utf-8', newline='') as file:
        csv_reader = list(csv.reader(file, delimiter=','))
        print(tabulate(csv_reader, headers='firstrow', tablefmt='github'))

    while True:
        quest = input(f'''{'-' * 60}
Enter:
 - 1, if you want to add a patient to the schedule;
 - 2, if you want to finish forming the schedule.
{'-' * 60}
''')

        if quest == '1':
            time = input('Enter the time you want to schedule the patient, it must be in the schedule (08:00): ')
            name = input('Enter the full name of patient separated by a space (Ivanov Ivan Ivanovich): ').title()
            f = add_patient_to_schedule(time, name)
            with open('src/schedule.csv', encoding='utf-8', newline='') as file:
                csv_reader = list(csv.reader(file, delimiter=','))
                print(tabulate(csv_reader, headers='firstrow', tablefmt='github'))

        elif quest == '2':
            break


if __name__ == '__main__':
    main()