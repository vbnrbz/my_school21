k = 0
s = ''

while k < 4:
    ind = input(f'{'-' * 50}\nEnter:\n - 1, if you want to add a patient to the waiting list;\n - 2, if you want to see the current queue.\n{'-' * 50}\n')
    if ind == '1':
        name = input('Enter the full name of patient: ')
        s += name + ', '
        k += 1
    elif ind == '2':
        print(f'Current queue - {s[:-2]}')
else:
    print(f'Current queue - {s[:-2]}', end='')
