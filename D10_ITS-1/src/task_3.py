from src.handler_3_file import FileHandler


def main():
    path = input('Enter the path to the file to read: ')

    example = FileHandler(path)
    print(f'{path} - {example.is_file_exists} ({example.type})')
    print(f'File extension - {example.file_extension}')
    print(example.read())

    new_example = FileHandler(input('Enter the path to the file to be written to: '))
    new_example.write('Test line')

if __name__ == '__main__':
    main()
