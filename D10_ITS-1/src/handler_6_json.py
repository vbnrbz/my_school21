from src.handler_6_file import FileHandler
import json


class JSONFileHandler(FileHandler):
    def read(self):
        with open(self.file_path, encoding='utf-8') as file:
            return json.load(file)

    def write(self, slovo):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(slovo, file, indent=4)

    def pretty_print(self, printer):
        print(f'Contents of the json file:\n{json.dumps(printer, indent=4)}')