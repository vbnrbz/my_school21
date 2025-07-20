"""
Пример кода с ошибкой №4
"""


input_int = input("Enter an integer: ")

if input_int.isdigit():
    print(f'Your number to the power of two is {int(input_int)**2}')
else:
    print('Well, I asked you to enter an integer! Come on!')


input_str = input("Now write this number again and add a letter to it: ")  # Например, 10а или 24ц.

# Попробуй дописать к этой строке фразу " - is not a number" и вывести на экран.
input_str += " - is not a number"
print(input_str)
