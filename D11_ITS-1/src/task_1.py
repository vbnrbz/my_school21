def main():
    quest = input(f'''Select what type of data you want to view:
 - 1, integer;
 - 2, float;
 - 3, bool.
''')

    first = input('Enter the first element: ')
    second = input('Enter the second element: ')

    if quest in ['1', '2', '3']:
        if quest == '1':
            first, second = int(first), int(second)
        elif quest == '2':
            first, second = float(first), float(int)
        elif quest == '3':
            first, second = bool(first), bool(second)

        print(f'ID of the first element ({first}) - {id(first)}')
        print(f'ID of the second element ({second}) - {id(second)}')
        print(f'element_1 is element_2 -> {first is second}')

if __name__ == '__main__':
    main()