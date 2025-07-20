import json
from typing import List, Dict, Any


def main(path: str) -> List[Dict[str, Any]]:
    with open(path, encoding='utf-8') as file:
        l: List[Dict[str, Any]] = json.load(file)
    l = sorted(l, key=lambda n: int(n['Age']), reverse=True)
    for ind, j in enumerate(l):
        j['ID'] = ind + 1
    return l


if __name__ == '__main__':
    path: str = 'materials/patients.json'
    main(path)
