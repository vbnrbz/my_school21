from src.handler_5_file import FileHandler
import csv


class CSVFileHandler(FileHandler):

    def read(self):
        with open(self.file_path, encoding='utf-8', newline='') as file:
            return list(csv.reader(file, delimiter=','))

    def write(self, slovo):
        with open(self.file_path, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file, delimiter=',')
            csv_writer.writerows(slovo)