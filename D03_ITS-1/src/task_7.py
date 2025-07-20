"""
Пример кода с ошибкой №7
"""


print('Program for visualization of indexes work\n')
test_string = 'Test string'
print(f'{test_string}\n')

ind_1 = input(
    'Enter the first index of the slice (or press Enter - '
    'this will mean that the slice is taken from the beginning of the line): '
)
ind_2 = input(
    'Enter the second index of the slice (or press Enter - '
    'this will mean that the slice is taken to the end of the line): '
)
step = input(
    'Enter the slice step (or press Enter - this will mean that the default step is 1): '
)

# Проверяем, не пустая ли строка в ind_1, ind_2, step. Если нет, то переводим в число эти переменные.
if ind_1:
    ind_1 = int(ind_1)
elif ind_1 == '':
    ind_1 = 0

if ind_2:
    ind_2 = int(ind_2)
elif ind_2 == '':
    ind_2 = len(test_string)

if step:
    step = int(step)
elif step == '':
    step = 1

# Напиши свой код тут, остальной код не трогай.
if ind_1 >= ind_2 or ind_1 > len(test_string) or ind_2 > len(test_string):
    raise IndexError("There is some kind of crap going on with your indexes!")

print('\nYour slice:')
if ind_1 and ind_2 and step:
    print(test_string[ind_1:ind_2:step])
elif (not ind_1) and ind_2 and step:
    print(test_string[:ind_2:step])
elif ind_1 and (not ind_2) and step:
    print(test_string[ind_1::step])
elif ind_1 and ind_2 and (not step):
    print(test_string[ind_1:ind_2])
elif (not ind_1) and (not ind_2) and step:
    print(test_string[::step])
elif ind_1 and (not ind_2) and (not step):
    print(test_string[ind_1::])
elif (not ind_1) and ind_2 and (not step):
    print(test_string[:ind_2:])
else:
    print(test_string[::])
