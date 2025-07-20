import sys


def main():
    def tuple_intern(some, d={}):
        if some in d:
            return d[some]
        else:
            d[some] = some
            return some

    quest = input(f'''Select what type of data you want to view:
 - 1, integer;
 - 2, float;
 - 3, bool;
 - 4, string;
 - 5, tuple.
''')

    if quest == '5':
        first = input('Enter the items for the first collection, separated by commas and spaces (in this form - 1, 2, 3): ').split(', ')
        second = input('Enter the items for the second collection, separated by commas and spaces (in this form - 1, 2, 3): ').split(', ')
    else:
        first = input('Enter the first element: ')
        second = input('Enter the second element: ')

    if quest in ['1', '2', '3', '4', '5']:
        if quest == '1':
            first, second = int(first), int(second)
        elif quest == '2':
            first, second = float(first), float(int)
        elif quest == '3':
            first, second = bool(first), bool(second)
        elif quest == '4':
            first, second = str(first), str(second)

            print(f'ID of the first element ({first}) - {id(first)}')
            print(f'ID of the second element ({second}) - {id(second)}')
            print(f'element_1 is element_2 -> {first is second}')
            print('-' * 50)

            first = sys.intern(first)
            second = sys.intern(second)

        elif quest == '5':
            first, second = tuple(first), tuple(second)

            print(f'ID of the first element ({first}) - {id(first)}')
            print(f'ID of the second element ({second}) - {id(second)}')
            print(f'element_1 is element_2 -> {first is second}')
            print('-' * 50)

            first = tuple_intern(first)
            second = tuple_intern(second)

        print(f'ID of the first element ({first}) - {id(first)}')
        print(f'ID of the second element ({second}) - {id(second)}')
        print(f'element_1 is element_2 -> {first is second}')

if __name__ == '__main__':
    main()
