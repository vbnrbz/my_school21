
def main():


    quest = input(f'''Select what type of data you want to view:
 - 1, integer;
 - 2, float;
 - 3, bool;
 - 4, string;
 - 5, tuple;
 - 6, list;
 - 7, set;
 - 8, frozen set;
 - 9, dict.
''')

    if quest in ['5', '6', '7', '8']:
        first = input('Enter the items for the first collection, separated by commas and spaces (in this form - 1, 2, 3): ').split(', ')
        second = input('Enter the items for the second collection, separated by commas and spaces (in this form - 1, 2, 3): ').split(', ')
    elif quest == '9':
        first = input('Enter key:value pairs for the first dictionary, separated by commas and spaces (in this form - 1:3, 2:4, 5:6 - separated by colons, without spaces between :): ').split(', ')
        second = input('Enter key:value pairs for the second dictionary, separated by commas and spaces (in this form - 1:3, 2:4, 5:6 - separated by colons, without spaces between :): ').split(', ')
    else:
        first = input('Enter the first element: ')
        second = input('Enter the second element: ')

    if quest in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if quest == '1':
            first, second = int(first), int(second)
        elif quest == '2':
            first, second = float(first), float(int)
        elif quest == '3':
            first, second = bool(first), bool(second)
        elif quest == '4':
            first, second = str(first), str(second)
        elif quest == '5':
            first, second = tuple(first), tuple(second)
        elif quest == '6':
            first, second = list(first), list(second)
        elif quest == '7':
            first, second = set(first), set(second)
        elif quest == '8':
            first, second = frozenset(first), frozenset(second)
        elif quest == '9':
            first = {i[:i.find(':')]: i[i.find(':')+1:] for i in first}
            second = {i[:i.find(':')]: i[i.find(':')+1:] for i in second}

        print(f'ID of the first element ({first}) - {id(first)}')
        print(f'ID of the second element ({second}) - {id(second)}')
        print(f'Element type - {type(first)}')
        print(f'element_1 == element_2 -> {first == second}')
        print(f'element_1 is element_2 -> {first is second}')

if __name__ == '__main__':
    main()
