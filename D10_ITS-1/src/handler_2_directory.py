import os
from src.handler_1_element import FileSystemElementHandler


class DirectoryHandler(FileSystemElementHandler):

    def __init__(self, file_path):
        super().__init__(file_path)
        self.children_files, self.children_directories = self.__get_directory_contents()

    def __get_directory_contents(self):

        if self.is_file_exists and self.type == 'directory':
                files = []
                dirs = []

                for i in os.listdir(self.file_path):
                    if os.path.isdir(f'{self.file_path}/{i}'):
                        dirs.append(i)
                    elif os.path.isfile(f'{self.file_path}/{i}'):
                        files.append(i)
        else:
            files = None
            dirs = None

        return files, dirs