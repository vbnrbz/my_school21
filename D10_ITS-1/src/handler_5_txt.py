from src.handler_5_file import FileHandler

class TXTFileHandler(FileHandler):

    def read(self):
        with open(self.file_path, encoding='utf-8') as file:
            return file.read()

    def write(self, slovo):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(slovo)