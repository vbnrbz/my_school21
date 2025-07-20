import os


class FileSystemElementHandler:

    def __init__(self, file_path):
        self.file_path = file_path
        self.is_file_exists = self.__element_exists()
        self.type = self.__get_element_type()

    def __element_exists(self):
        return os.path.exists(self.file_path)

    def __get_element_type(self):
        if os.path.exists(self.file_path):
            if os.path.isfile(self.file_path):
                return 'file'
            elif os.path.isdir(self.file_path):
                return 'directory'
        else:
            return None