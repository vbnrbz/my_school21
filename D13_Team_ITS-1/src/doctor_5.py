import json
import os
from src.config_4 import Configuration
from typing import Dict, Optional, List


class Doctor:
    def __init__(self, config: Configuration) -> None:
        self.config: Configuration = config

        with open(f'{self.config.base_folder}/{self.config.login}.json', encoding='utf-8') as file:
            x: Dict[str, str] = json.load(file)
            name: str = x['Surname'] + ' ' + x['Name'] + ' ' + x['Patronymic']
            speciality: str = x['Speciality']

        self.name: str = name
        self.speciality: str = speciality


    def __write_receipt_to_file(self, rec: str, file_name: str) -> None:
        os.makedirs('config.base_folder', exist_ok=True)
        with open(f'config.base_folder/{file_name}.txt', 'w', encoding='utf-8') as file:
            file.write(rec)

    def write_recipe(self, file_name: Optional[str] = None) -> str:
        print('Enter recipe (to finish press Enter twice): ')
        l: List[str] = list()
        l.append(input())
        k: int = 0
        if l[0] == '':
            k += 1

        while k < 2:
            l.append(input())
            if l[-1] == '':
                k += 1
            else:
                k = 0

        l[-1] = self.name
        l.append(f'Doctor-{self.speciality}')

        if file_name is not None:
            self.__write_receipt_to_file('\n'.join(l), file_name)

        return '\n'.join(l)
