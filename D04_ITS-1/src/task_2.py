k = 0
s = ''

while k < 4:
    ind = input(f'{'-' * 50}\nEnter:\n - 1, if you want to add a patient to the waiting list;\n - 2, if you want to see the current queue.\n - 3, if you want to terminate the program and see the resulting queue.\n{'-' * 50}\n')
    if ind == '1':
        name = input('Enter the full name of patient: ')
        s += name.title() + ', '
        k += 1
    elif ind == '2':
        if s:
            print(f'Current queue - {s[:-2]}')
        else:
            print('The queue is empty!')
    elif ind == '3':
        if s:
            print(f'Current queue - {s[:-2]}', end='')
        else:
            print('The queue is empty!', end='')
        break
else:
    print(f'The queue is full!\nCurrent queue - {s[:-2]}', end='')
