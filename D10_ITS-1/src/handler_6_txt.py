from src.handler_6_file import FileHandler

class TXTFileHandler(FileHandler):

    def read(self):
        with open(self.file_path, encoding='utf-8') as file:
            return file.read()

    def write(self, slovo):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(slovo)

    def pretty_print(self, printer):
        print(f'Contents of the text file:\n{printer}')