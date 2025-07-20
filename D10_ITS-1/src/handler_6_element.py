import os


class FileSystemElementHandler:

    def __init__(self, file_path):
        self.file_path = file_path
        self.is_file_exists = self.element_exists(self.file_path)
        self.type = self.get_element_type(self.file_path)

    @classmethod
    def element_exists(cls, path):
        return os.path.exists(path)

    @classmethod
    def get_element_type(cls, path):
        if os.path.exists(path):
            if os.path.isfile(path):
                return 'file'
            elif os.path.isdir(path):
                return 'directory'
        else:
            return None