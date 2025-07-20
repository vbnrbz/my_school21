import copy
import json
from typing import Dict, List, Tuple, Any


def main(path: str) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    with open(path, encoding='utf-8') as file:
        l: List[Dict[str, Any]] = json.load(file)
    l_1: List[Dict[str, Any]] = copy.deepcopy(l)
    l_2: List[Dict[str, Any]] = copy.deepcopy(l)
    l_3: List[Dict[str, Any]] = copy.deepcopy(l)
    x: List[Dict[str, Any]] = list(filter(lambda n: n['Sex'] == 'Man', l_1))
    y: List[Dict[str, Any]] = list(filter(lambda n: n["Chronic diseases"] == [], l_2))
    z: List[Dict[str, Any]] = list(filter(lambda n: int(n['Age']) < 50, l_3))
    return x, y, z


if __name__ == '__main__':
    path: str = 'materials/patients.json'
    main(path)
