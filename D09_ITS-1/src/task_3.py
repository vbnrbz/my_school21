from src.schedule_3 import Schedule


def main():
    for i in range(2):
        name = input('Enter the full name of the first doctor: ').title()
        spec = input('Enter the speciality of the first doctor: ').title()
        start = input('Enter the time of first appointment (08:00): ')
        end = input('Enter the time of last appointment (13:30): ')
        step = int(input('Enter the duration of one appointment in minutes (15): '))
        print('-' * 50)
        if i == 0:
            medic_1 = Schedule(name, spec, start, end, step)
        elif i == 1:
            medic_2 = Schedule(name, spec, start, end, step)

    l_1 = medic_1.get_list_timestamps_for_schedule()
    l_2 = medic_2.get_list_timestamps_for_schedule()

    print(f'First list of timestamps - {l_1}')
    print(f'Second list of timestamps - {l_2}')

if __name__ == '__main__':
    main()