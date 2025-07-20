from src.schedule_5 import Schedule


def main():
    d = {}
    while True:
        quest = input(f'''{'-' * 50}
Enter:
 - 1, if you want to create a schedule;
 - 2, if you want to complete the program.       
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
            for i in d.values():
                i.write_to_csv()
            break


if __name__ == '__main__':
    main()