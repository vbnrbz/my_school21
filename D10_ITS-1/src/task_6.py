from src.handler_5_file import FileHandler
from src.handler_6_csv import CSVFileHandler
from src.handler_6_json import JSONFileHandler
from src.handler_6_txt import TXTFileHandler


def main():
    path = input('Enter the path to the file to read: ')
    a = TXTFileHandler(path)
    if a.is_file_exists:
        if a.type == 'file':
            ext = a.file_extension
            if ext == 'txt':
                printer = TXTFileHandler(path)
                printer.pretty_print(printer.read())
            elif ext == 'json':
                printer = JSONFileHandler(path)
                printer.pretty_print(printer.read())
            elif ext == 'csv':
                printer = CSVFileHandler(path)
                printer.pretty_print(printer.read())
        else:
            print('This is not a file, but a folder!')
    else:
        print('There is no such file!')

if __name__ == '__main__':
    main()