"""
Пример кода с ошибкой №6
"""
import sys


print('Program for visualization of indexes work\n')
test_string = 'Test string'
print(test_string)

# Представь, что пользователь всегда точно вводит 0 или 1. Случай, когда он введет что-то другое, не обрабатывай.
is_index_flag = bool(int(input('\nEnter\n - 0, if you want to stop the program;\n - 1, if you want to set the index.\n')))

if is_index_flag:
    index = int(input('Enter the index: '))
    try:
        print(f'The element at this index - "{test_string[index]}"')
    except IndexError:
        print('There is no such index in this line!')
    else:
        print('And yes, such an index really did exist!')
    finally:
        print('End!')

else:
    sys.exit()
