from src.utils import get_list_timestamps_for_schedule, create_schedule
from tabulate import tabulate


def main():
    start = input('Enter the time of first appointment (08:00): ')
    end = input('Enter the time of last appointment (13:30): ')
    step = input('Enter the duration of one appointment in minutes (15): ')
    default_value = input('Enter the text that will be displayed in the column "The patient visited the doctor" by default (if you just press Enter, the default will be "No"): ')

    res_1 = get_list_timestamps_for_schedule(start, end, step)
    res_2 = create_schedule(res_1, default_value)

    print(tabulate(res_2, headers='firstrow', tablefmt='github'))


if __name__ == '__main__':
    main()