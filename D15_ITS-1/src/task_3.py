import copy
import json
from typing import Dict, Any, List, Tuple


def anonymize_patient(d: Dict[str, Any]) -> Dict[str, Any]:
    d.pop('Name')
    d.pop('Surname')
    d.pop('Patronymic')
    return d


def change_blood_type(d: Dict[str, Any]) -> Dict[str, Any]:
    blood = {
        "O+": "I+",
        "A+": "II+",
        "B+": "III+",
        "AB+": "IV+",
        "O-": "I-",
        "A-": "II-",
        "B-": "III-",
        "AB-": "IV-"
    }
    d['Blood group'] = blood[d['Blood group']]
    return d


def change_type_age(d: Dict[str, Any]) -> Dict[str, Any]:
    d['Age'] = int(d['Age'])
    return d


def main(path: str) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    with open(path, encoding='utf-8') as file:
        l: List[Dict[str, Any]] = json.load(file)
    l_d_1: List[Dict[str, Any]] = copy.deepcopy(l)
    l_d_2: List[Dict[str, Any]] = copy.deepcopy(l)
    l_d_3: List[Dict[str, Any]] = copy.deepcopy(l)
    x: List[Dict[str, Any]] = list(map(anonymize_patient, l_d_1))
    y: List[Dict[str, Any]] = list(map(change_blood_type, l_d_2))
    z: List[Dict[str, Any]] = list(map(change_type_age, l_d_3))
    return x, y, z


if __name__ == '__main__':
    path: str = 'materials/patients.json'
    main(path)
