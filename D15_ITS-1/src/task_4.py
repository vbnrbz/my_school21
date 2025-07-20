import copy
import json
from typing import Dict, Any, List, Tuple, Optional


def filter_by_man(d: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    return d if d['Sex'] == "Man" else None


def filter_by_absence_illness(d: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    return d if d["Chronic diseases"] == [] else None


def filter_by_age(d: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    return d if int(d['Age']) < 50 else None


def process_patients(func, l_d: List[Dict[str, Any]]):
    new_l_d: List[Dict[str, Any]] = copy.deepcopy(l_d)
    return [func(i) for i in new_l_d if func(i) is not None]


def main(path: str) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    with open(path, encoding='utf-8') as file:
        l: List[Dict[str, Any]] = json.load(file)
    x: List[Dict[str, Any]] = process_patients(filter_by_man, l)
    y: List[Dict[str, Any]] = process_patients(filter_by_absence_illness, l)
    z: List[Dict[str, Any]] = process_patients(filter_by_age, l)
    return x, y, z


if __name__ == '__main__':
    path: str = 'materials/patients.json'
    main(path)
