from src.handler_6_file import FileHandler
import csv
from tabulate import tabulate


class CSVFileHandler(FileHandler):

    def read(self):
        with open(self.file_path, encoding='utf-8', newline='') as file:
            return list(csv.reader(file, delimiter=','))

    def write(self, slovo):
        with open(self.file_path, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file, delimiter=',')
            csv_writer.writerows(slovo)

    def pretty_print(self, printer):
        print(f'Contents of the csv file:\n{tabulate(printer, headers="firstrow", tablefmt="github")}')