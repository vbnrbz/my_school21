"""
Пример кода с ошибкой №5
"""
from random import randint  # И опять повод загуглить незнакомый модуль.
import math


input_number = int(input('Enter an integer between -10 and 10: '))

random_number = randint(-10, 10)
print(f'Random number = {random_number}')

difference_numbers = input_number - random_number
print(f'{input_number} - ({random_number}) = {difference_numbers}')

try:
    sqrt_number = round(math.sqrt(difference_numbers), 2)
    print(f'Root of {difference_numbers} = {sqrt_number}')
except ValueError:
    print('You can not take the root of a negative number!')


