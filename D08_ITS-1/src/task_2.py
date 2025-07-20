from src.utils import get_list_timestamps_for_schedule


def main():
    start = input('Enter the time of first appointment (08:00): ')
    end = input('Enter the time of last appointment (13:30): ')
    step = input('Enter the duration of one appointment in minutes (15): ')

    res = get_list_timestamps_for_schedule(start, end, step)
    print(res)

if __name__ == '__main__':
    main()