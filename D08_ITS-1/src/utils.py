from datetime import timedelta, datetime
import csv

def get_list_timestamps_for_schedule(start, end, step):
    my_list = []
    start = datetime.strptime(start, '%H:%M')
    end = datetime.strptime(end, '%H:%M')
    step = int(step)

    while start <= end:
        my_list.append(start.strftime('%H:%M'))
        start += timedelta(minutes=step)

    return my_list

def create_schedule(timestamps, default_value='No'):
    my_list = [['Time', 'Patient', 'The patient visited the doctor']]

    for i in range(len(timestamps)):
        my_list.append([timestamps[i], '', default_value])

    with open('src/schedule.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(my_list)

    return my_list

def add_patient_to_schedule(time, patient):
    with open('src/schedule.csv', encoding='utf-8', newline='') as file:
        reader = list(csv.reader(file, delimiter=','))
    k = 0
    for i in range(len(reader)):
        if time in reader[i]:
            k += 1
            reader[i][1] = patient
    if k == 0:
        print('This time is not on the schedule!')
    else:
        with open('src/schedule.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(reader)

    return reader

def add_tech_times_to_schedule(*times):
    with open('src/schedule.csv', encoding='utf-8', newline='') as file:
        reader = list(csv.reader(file, delimiter=','))
    k = 0
    for i in range(len(reader)):
        for j in times:
            if j in reader[i]:
                k += 1
                reader[i][1] = 'Technical time'

    if k != 0:
        with open('src/schedule.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(reader)

    return reader