from src.handler_5_csv import CSVFileHandler
from src.handler_5_txt import TXTFileHandler
from src.handler_5_json import JSONFileHandler



def main():
    path = input('Enter the path to the csv file to read: ')
    example = CSVFileHandler(path)
    print(f'{path} - {example.is_file_exists} ({example.type})')
    print(f'File extension - {example.file_extension}')
    print(example.read())

    new_example = CSVFileHandler(input('Enter the path to the csv file to be written to: '))
    new_example.write([['a', 'b'], [0, 1], [2, 3]])

if __name__ == '__main__':
    main()