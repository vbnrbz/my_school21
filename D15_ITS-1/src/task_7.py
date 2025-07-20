import json
from typing import List, Dict, Any


def main(path: str) -> List[Dict[str, Any]]:
    with open(path, encoding='utf-8') as file:
        l: List[Dict[str, Any]] = json.load(file)
    keys: List[Any] = ['ID', 'Name', 'Surname', 'Patronymic', 'Age', 'Sex', 'Blood group', 'Chronic diseases']
    values: List[Any] = [11, 'Vasiliy', 'Vasiliev', 'Vasilievich', '48', 'Man', 'O-', ['Haemorrhoids']]
    l.append(dict(zip(keys, values)))
    return l


if __name__ == '__main__':
    path: str = 'materials/patients.json'
    main(path)
