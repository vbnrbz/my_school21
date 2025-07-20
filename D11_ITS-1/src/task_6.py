import copy

def example_1():
    print('Пример 1')
    a = [1, 2, 3, 4, 5]
    b = a[:]
    b.append(10)
    print(a is b)
    print(a)
    print(b)
    print('-'*50)

def example_2():
    print('Пример 2')
    a = [[1, 2, 3], [4, 5, 6]]
    b = copy.deepcopy(a)
    b[0][0] = 10
    print(a is b)
    print(a)
    print(b)
    print('-' * 50)


def example_3():
    print('Пример 3')
    a = {'a': [1, {'b': [10, 20]}, 3], 'b': [1, {'c': 3}, 4]}
    b = copy.deepcopy(a)
    b['b'][1] = 10
    print(a is b)
    print(a)
    print(b)
    print('-' * 50)


def main():
    example_1()
    example_2()
    example_3()


if __name__ == '__main__':
    main()
