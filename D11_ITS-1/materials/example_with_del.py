def main():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [a, b]
    del a
    del b
    print(c)


if __name__ == '__main__':
    main()
