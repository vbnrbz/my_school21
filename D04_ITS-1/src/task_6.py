s = dict()

while len(s) < 4:
    ind = input(f'''{'-' * 50}
Enter:
 - 1, if you want to add a patient to the waiting list;
 - 2, if you want to remove a patient from the queue;
 - 3, if you want to see the current queue;
 - 4, if you want to terminate the program and see the resulting queue.
{'-' * 50}
''')

# FIRST OPTION!!!
    if ind == '1':
        time_and_name = input('Enter the time and the full name of patient (comma and space - 08:00, Ivanov A.A.): ').split(', ')
        time = time_and_name[0]
        name = time_and_name[1].title()

        if time in s:
            print('That time is already taken!')
        elif name in s.values():
            print('This patient is already on the waiting list!')
        else:
            s[time] = name

# SECOND OPTION!!!
    elif ind == '2':
        ind_two = input(f'''{'-' * 50}
Enter:
 - 1, if you want to time-delay a patient;
 - 2, if you want to delete a patient by full name.
{'-' * 50}
''')
        if ind_two == '1':
            time = input('Enter the time of the patient to be removed from the queue (e.g. 08:00 or 10:15): ')
            if time not in s.keys():
                print('This time is free!')
            else:
                s.pop(time)

        elif ind_two == '2':
            name = input('Enter the full name (or part of the full name) of the patients you want to remove from the queue: ')

            new_s = s.copy()
            for i, j in s.items():
                if j.lower().startswith(name.lower()):
                    new_s.pop(i)
            if len(new_s) == len(s):
                print('Those patients are not on the waiting list!')
            s = new_s.copy()

# THIRD OPTION!!!
    elif ind == '3':
        if s:
            print(f'Current queue - {s}')
        else:
            print('The queue is empty!')

# FORTH OPTION!!!
    elif ind == '4':
        if s:
            print(f'Current queue - {s}', end='')
        else:
            print('The queue is empty!', end='')
        break

else:
    print(f'The queue is full!\nCurrent queue - {s}', end='')
