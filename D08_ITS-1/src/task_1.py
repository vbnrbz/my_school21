from datetime import timedelta, datetime


def get_list_timestamps_for_schedule(start, end, step):
    my_list = []
    start = datetime.strptime(start, '%H:%M')
    end = datetime.strptime(end, '%H:%M')
    step = int(step)

    while start <= end:
        my_list.append(start.strftime('%H:%M'))
        start += timedelta(minutes=step)

    return my_list


start = input('Enter the time of first appointment (08:00): ')
end = input('Enter the time of last appointment (13:30): ')
step = input('Enter the duration of one appointment in minutes (15): ')

res = get_list_timestamps_for_schedule(start, end, step)
print(res)

