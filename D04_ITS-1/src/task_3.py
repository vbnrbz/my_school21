s = set()

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
        name = input('Enter the full name of patient: ').title()
        s.add(name)

# SECOND OPTION!!!
    elif ind == '2':
        name = input('Enter the name of the patient to be removed from the queue: ').title()
        if name in s:
            s.remove(name)
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
