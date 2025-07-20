from src.handler_4_json import JSONFileHandler


def main():
    path = input('Enter the path to the json file to read: ')

    example = JSONFileHandler(path)
    print(f'{path} - {example.is_file_exists} ({example.type})')
    print(f'File extension - {example.file_extension}')
    print(example.read())

    new_example = JSONFileHandler(input('Enter the path to the json file to be written to: '))
    new_example.write({1: 'Test 1', 2: 'Test 2'})


if __name__ == '__main__':
    main()
