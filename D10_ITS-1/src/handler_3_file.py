from src.handler_1_element import FileSystemElementHandler


class FileHandler(FileSystemElementHandler):

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_extension = self.__get_file_extension()

    def __get_file_extension(self):
        return self.file_path[self.file_path.rfind('.')+1:]

    def read(self):
        with open(self.file_path, encoding='utf-8') as file:
            return file.read()

    def write(self, slovo):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(slovo)