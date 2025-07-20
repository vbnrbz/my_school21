
def main():
    def pretty_print(x):
        print('Before the change:')
        print(f'The element - {x}')
        print(f'ID - {id(x)}')
        print('-' * 50)

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
        first = input('Enter the items for the collection, separated by commas and spaces (in this form - 1, 2, 3): ').split(', ')
    elif quest == '9':
        first = input('Enter key:value pairs for the dictionary, separated by commas and spaces (in this form - 1:3, 2:4, 5:6 - separated by colons, without spaces between :): ').split(', ')
    else:
        first = input('Enter the element: ')

    if quest in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if quest == '1':
            first = int(first)
            id_first = id(first)
            pretty_print(first)
            first -= 100
        elif quest == '2':
            first = float(first)
            id_first = id(first)
            pretty_print(first)
            first -= 100
        elif quest == '3':
            first = bool(first)
        elif quest == '4':
            first = str(first)
            id_first = id(first)
            pretty_print(first)
            first += '-100'
        elif quest == '5':
            first = tuple(first)
            id_first = id(first)
            pretty_print(first)
            first += (-100,)
        elif quest == '6':
            first = list(first)
            id_first = id(first)
            pretty_print(first)
            first.append(-100)
        elif quest == '7':
            first = set(first)
            id_first = id(first)
            pretty_print(first)
            first.add(-100)
        elif quest == '8':
            first = frozenset(first)
            id_first = id(first)
            pretty_print(first)
            first |= frozenset((-100,))
        elif quest == '9':
            first = {i[:i.find(':')]: i[i.find(':')+1:] for i in first}
            id_first = id(first)
            pretty_print(first)
            first['-100'] = -100

        print('After the change:')
        print(f'The element - {first}')
        print(f'ID - {id(first)}')
        print('-' * 50)
        print(f'element_before is element_after -> {id(first) == id_first}')


if __name__ == '__main__':
    main()
