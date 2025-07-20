s = []

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
        ind_one = input(f'''{'-' * 50}
Enter:
 - 1, if you want to add a patient to the back of the queue;
 - 2, if you want to add a patient to the beginning or middle of the queue.
{'-' * 50}
''')
        name = input('Enter the full name of patient: ').title()

        if name in s:
            print('This patient is already on the waiting list!')
        elif name not in s and ind_one == '1':
            s.append(name)
        elif name not in s and ind_one == '2':
            a = int(input('Specify where in the queue you want to place the patient: '))
            s.insert(a-1, name)

# SECOND OPTION!!!
    elif ind == '2':
        ind_two = input(f'''{'-' * 50}
Enter:
 - 1, if you want to delete a patient by full name;
 - 2, if you want to remove a patient by his or her number in the queue.
''')
        if ind_two == '1':
            name = input('Enter the full name of patient: ').title()
            if name in s:
                s.remove(name)
            else:
                print('This patient is not in the waiting list!')
        elif ind_two == '2':
            a = int(input('Enter the queue number of the person: '))
            if 0 < a <= len(s):
                s.pop(a - 1)
            else:
                print('This patient is not in the waiting list!')

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
