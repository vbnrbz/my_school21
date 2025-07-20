from src.handler_5_file import FileHandler
import json


class JSONFileHandler(FileHandler):
    def read(self):
        with open(self.file_path, encoding='utf-8') as file:
            x = json.load(file)
            return json.dumps(x)

    def write(self, slovo):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(slovo, file, indent=4)