from src.handler_2_directory import DirectoryHandler


def main():
    path = input('Enter the path to the folder: ')
    example = DirectoryHandler(path)
    print(f'{path} - {example.is_file_exists} ({example.type})')
    print(f'Inside {path} are:')
    print(f'Folder - {example.children_directories}')
    print(f'Files - {example.children_files}')


if __name__ == '__main__':
    main()

