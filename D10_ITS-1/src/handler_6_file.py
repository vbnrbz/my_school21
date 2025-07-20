from src.handler_6_element import FileSystemElementHandler
from abc import ABC, abstractmethod


class FileHandler(FileSystemElementHandler, ABC):

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_extension = self.get_file_extension(self.file_path)

    @classmethod
    def get_file_extension(cls, path):
        return path[path.rfind('.')+1:]

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, new_path):
        pass

    @abstractmethod
    def pretty_print(self, printer):
        pass