from src.handler_1_element import FileSystemElementHandler
from abc import ABC, abstractmethod


class FileHandler(FileSystemElementHandler, ABC):

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_extension = self.__get_file_extension()

    def __get_file_extension(self):
        return self.file_path[self.file_path.rfind('.')+1:]

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, new_path):
        pass