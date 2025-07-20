from src.schedule_6 import Schedule


def main():
    d = {}
    while True:
        quest = input(f'''{'-' * 50}
Enter:
 - 1, if you want to create a schedule;
 - 2, if you want to add a patient to a ready schedule;
 - 3, if you want to complete the program.   
{'-' * 50}
''')
        if quest == '1':
            name = input('Enter the full name of the first doctor: ').title()
            spec = input('Enter the speciality of the first doctor: ').title()
            start = input('Enter the time of first appointment (08:00): ')
            end = input('Enter the time of last appointment (13:30): ')
            step = int(input('Enter the duration of one appointment in minutes (15): '))
            print('-' * 50)
            d[name] = Schedule(name, spec, start, end, step)

        elif quest == '2':
            print(f'List of current schedules - {', '.join(i for i in d)}')
            doctor = input('Enter the full name of the doctor to whose schedule you want to add the patient: ').title()
            print(f'Doctor - {doctor}\nSpeciality - {d[doctor].doctor_speciality}')
            d[doctor].print_schedule()

            time = input('Enter the time you want to schedule the patient, it must be in the schedule (08:00): ')
            pacient = input('Enter the full name of patient separated by a space (Ivanov Ivan Ivanovich): ').title()
            d[doctor].add_patient_to_schedule(time, pacient)
            d[doctor].print_schedule()

        elif quest == '3':
            for i in d.values():
                i.write_to_csv()
            break


if __name__ == '__main__':
    main()