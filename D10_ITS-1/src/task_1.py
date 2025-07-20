from src.handler_1_element import FileSystemElementHandler


def main():
    path = input('Enter the path to the file or folder: ')
    example = FileSystemElementHandler(path)
    print(f'{path} - {example.is_file_exists} ({example.type})')

if __name__ == '__main__':
    main()